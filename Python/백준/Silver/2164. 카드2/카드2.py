from collections import deque
N=int(input())
que=deque(range(1,N+1))
while len(que)>1:
    # 첫 인자를 꺼내고 없엔다.
    pop_1=que.popleft()
    # 두번 째 인자를 꺼내고 마지막에 넣는다.
    que.append(que.popleft())
print(que[0])