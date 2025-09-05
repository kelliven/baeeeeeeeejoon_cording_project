from collections import deque
import sys

N=int(sys.stdin.readline())
que=deque()
def push(X):
    que.append(X)
def pop():
    if que:print(que.popleft())
    else:print('-1')
def size():print(len(que))
def empty():
    if que:print(0)
    else:print(1)
def front():
    if que:print(que[0])
    else:print(-1)
def back():
    if que:print(que[-1])
    else:print(-1)
    
s={'push':push,'pop':pop,'size':size,'empty':empty,'front':front,'back':back}

for _ in range(N):
    cmd=sys.stdin.readline().split()
    if cmd[0]=='push':
        s['push'](cmd[1])
    else:
        s[cmd[0]]()