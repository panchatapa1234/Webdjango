def fact(n):
    f=1
    if(n==0 or n==1):
        return 1
    return f*fact(n-1)
print(fact(5))    