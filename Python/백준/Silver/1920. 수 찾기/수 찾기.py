import sys
input=sys.stdin.readline
n=int(input())
nl=set(map(int,input().split()))
m=int(input())
ml=list(map(int,input().split()))
for i in range(m):
    if ml[i] in nl:print("1")
    else:print("0")