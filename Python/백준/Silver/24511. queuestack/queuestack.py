from collections import deque
N=int(input())
A=input().split()
B=input().split()
M=int(input())
C=input().split()
que=deque()
for i in range(N):
    if A[i]=='0':
        que.append(B[i])
for i in range(M):
    que.appendleft(C[i])
    print(que.pop(),end=' ')