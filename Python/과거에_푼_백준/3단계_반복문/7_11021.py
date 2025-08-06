import sys
T=int(input())
C=[]
a=[]
b=[]
for _ in range(T):
    A,B=map(int, sys.stdin.readline().split())
    C.append(A+B)
    a.append(A)
    b.append(B)
for i in range(T):
    print('Case #%d: %d + %d = %d'%(i+1,a[i],b[i],C[i]))