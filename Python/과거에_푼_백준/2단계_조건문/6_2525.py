A,B=map(int,input().split())
C=int(input())
a,b=[C//60,C%60]
if 0<=A+a<24:
    if B+b<60:
        print(A+a,B+b)
    else:
        if A+a!=23:print(A+a+1,B+b-60)
        else:print(0,B+b-60)
elif A+a>23:
    if B+b<60:print((A+a)-24,B+b)
    else:print((A+a)-23,(B+b)-60)