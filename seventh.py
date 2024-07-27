L1=eval(input("Enter Set One"))
L2=eval(input("Enter Set Two"))
I=[]
M=[]
T1=[]
T2=[]
for i in L1:
    if(i in L2):
        I.append(i)
    else:
        T1.append(i)
        M.append(T1)  
for i in L2:
    if(i in L1):
        T2.append(i) 
        M.append(i)  
print(I,M,T1,T2)
if L2 in L1:
    print("Superset is L1 and subset is L2")
else:
    print("Superset is L2 and subset is L1")