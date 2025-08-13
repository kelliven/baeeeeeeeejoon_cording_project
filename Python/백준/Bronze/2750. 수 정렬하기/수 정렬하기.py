N=int(input())
A=[]
for i in range(N):
    A.append(int(input()))
B=sorted(A)
for j in range(N):
    print(B[j])