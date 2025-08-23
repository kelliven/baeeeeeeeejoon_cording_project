import sys
input=sys.stdin.readline
ans=0
N,M=map(int,input().split())
N_Set={input().strip() for _ in range(N)}
for _ in range(M):
    if input().strip() in N_Set:
        ans+=1
print(ans)