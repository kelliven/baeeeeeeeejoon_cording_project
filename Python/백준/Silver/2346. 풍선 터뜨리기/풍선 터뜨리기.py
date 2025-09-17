from collections import deque
import sys
N=int(sys.stdin.readline())
ball=deque(enumerate(map(int,input().split())))
sex=[]
while ball:
    a,b=ball.popleft()
    sex.append(a+1)
    if b>0:
        ball.rotate(-(b-1))
    else:
        ball.rotate(-b)
print(*sex)