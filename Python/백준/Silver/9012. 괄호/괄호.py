import sys
input=sys.stdin.readline
n=int(input())
count=0
for i in range(n):
    x=list(input().strip())
    count=0
    ok=True
    for j in x:
        if j=='(':
            count+=1
        else:
            count-=1
            if count < 0:
                ok=False
                break
    if ok and count==0:
        print('YES')
    else:print('NO')