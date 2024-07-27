n=int(input())
L=[]
for i in range(0,n):
    L.append(int(input()))
print(L)
for i in L:
    dn=i
    r=0
    while(dn>0):
      r=int(r*10)+int(dn%10) 
      dn=int(dn/10)
    print(r)
    