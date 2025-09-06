from collections import deque
N,K=map(int,input().split())
d_que=deque([i for i in range(1,N+1)])
yeoman=[]
for _ in range(N):
    d_que.rotate(-(K-1))
    yeoman.append(d_que[0])
    d_que.popleft()
print("<"+", ".join(map(str,yeoman))+">")