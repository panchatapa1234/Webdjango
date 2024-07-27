def avg(*n):
    s=0
    for x in n:
        s=s+x
    return s/len(n)
x=avg(20,25,65,80)
print("Average :",x)
