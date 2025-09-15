from collections import deque
import sys
N=int(input())
deck=deque()
for _ in range(N):
    cmd=sys.stdin.readline().split()
    if cmd[0]=='1':deck.appendleft(cmd[1])
    elif cmd[0]=='2':deck.append(cmd[1])
    elif cmd[0]=='3':print(deck.popleft() if deck else '-1')
    elif cmd[0]=='4':print(deck.pop() if deck else '-1')
    elif cmd[0]=='5':print(len(deck))
    elif cmd[0]=='6':print('1' if not deck else '0')
    elif cmd[0]=='7':print(deck[0] if deck else '-1')
    else: print(deck[-1] if deck else '-1')