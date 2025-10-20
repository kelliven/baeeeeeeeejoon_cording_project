import sys
input=sys.stdin.readline
N,K=map(int,input().split())
coin_list=[]
count=0
for _ in range(N):
    coin_list.append(int(input()))
for i in coin_list[::-1]:
    if K//i!=0:
        count+=K//i
        K%=i
print(count)