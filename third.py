n=int(input("Enter the number of years :"))
L1=[]
s=0
print("Enter the sgpa :")
for i in range(0,2*n):
    m=int(input())
    L1.append(m)
    s=s+m
c=s/(2*n)
print("cgpa =",c)    