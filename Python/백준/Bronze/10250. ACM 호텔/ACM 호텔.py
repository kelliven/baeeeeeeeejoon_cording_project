T=int(input())
for _ in range(T):
    H,W,N=map(int,input().split())
    x=0
    for i in range(1,W+1):
        for j in range(1,H+1):
            x+=1
            if N==x:
                room=j*100+i
    print(room)