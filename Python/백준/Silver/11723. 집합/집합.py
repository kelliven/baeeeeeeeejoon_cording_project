import sys
S=set()
N=int(sys.stdin.readline())
for _ in range(N):
    cmd=sys.stdin.readline().strip().split()
    if len(cmd)==1:
        if cmd[0]=='all':
            S={i for i in range(1,21)}
        elif cmd[0]=='empty':
            S=set()
    else:
        a,x=cmd[0],int(cmd[1])
        if a=='add':
            S.add(x)
        elif a=='remove':
            S.discard(x)
        elif a=='check':
            if x in S:
                print(1)
            else:print(0)
        elif a=='toggle':
            if x in S:
                S.discard(x)
            else:S.add(x)