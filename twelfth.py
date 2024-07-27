s=lambda a:1 if a==0 else a*s(a-1)
print("Factorial :",s(5))