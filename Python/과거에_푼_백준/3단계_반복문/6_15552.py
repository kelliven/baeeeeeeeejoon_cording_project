import sys
T=int(input())
C=[]
for _ in range(T):
    A,B=map(int, sys.stdin.readline().split())
    C.append(A+B)
for i in range(T):
    print(C[i])