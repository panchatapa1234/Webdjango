a=int(input())
c=0
try:
    i=2
    while(i<=a/2):
        if(a%i==0):
            c=1
            break
        i=i+1
    if(c==0):
        print("Prime")
    else:
        print("Not Prime")
except:
    print("Invalid Input") 