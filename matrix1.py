#transpose of matrix
n,m=map(int,input("enetr the dimensions nxm:").lower().split('x'))
def show(x):
    for var in x:
        s='{:10}'*len(var)
        print('\t',s.format(*var))
print("please give me mat A:")
A=[list(map(int,input('\t').split()))for var in range(n)]
print("please give me mat B:")
B=[list(map(int,input('\t').split()))for var in range(n)]
print("mat A is:")
show(A)
print("mat B is:")
show(B)
r=A[[n][m]]
for m in range(len(A)):
    for n in range(len(0)):
        r[n][m]=A[m][n]
for r in result:
    print(r)
        
