from django.shortcuts import render,redirect
from .models import UsersTable
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login as auth_login
def login(request):
 if request.method == 'POST':
   email = request.POST['email']
   password = request.POST['password']
   try:
      user = UsersTable.objects.get(email=email)
      if check_password(password,user.password):
         auth_login(request,user)
         return redirect('home')
      else:
         return render(request,'login.html',{'error' : 'Invalid Password'})
   except UsersTable.DoesNotExist:
      return render(request,'login.html', {'error' : 'Email Does Not Exist'})
 else:
    return render(request, 'login.html')
  
         

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        hashed_password = make_password(password)
        user = UsersTable( email = email, password = hashed_password)
        user.save()
        return redirect('login')
    else:
        return render(request, 'register.html')
def home(request):
   return render(request, 'home.html')    