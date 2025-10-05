N=int(input())
A=list(map(int,input().split()))
s=0
for i in A:
    for x in range(2,i+1):
        if i%x==0:
            if i==x:
                s+=1
            break
print(s)