def sum(n):
    if n==1 :
        return 1
    else:
        return n + sum(n-1)
result = sum(5)
print("Sum received :",result)   