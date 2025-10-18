import sys
input=sys.stdin.readline
N=int(input())
stk=[]
for i in range(N):
    cmd=input().split()
    if cmd[0]=='push':
        stk.append(int(cmd[1]))
    elif cmd[0]=='pop':
        if not stk:
            print(-1)
        else:print(stk.pop(-1))
    elif cmd[0]=='size':
        print(len(stk))
    elif cmd[0]=='empty':
        if stk:print(0)
        else:print(1)
    elif cmd[0]=='top':
        if stk:print(int(stk[-1]))
        else:print(-1)