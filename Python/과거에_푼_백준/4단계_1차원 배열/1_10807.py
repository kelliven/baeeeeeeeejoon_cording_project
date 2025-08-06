N=int(input())
a=list(map(int, input().split()))
v=int(input())
count=0
for i in a:
    if v==i:
        count+=1
print(count)