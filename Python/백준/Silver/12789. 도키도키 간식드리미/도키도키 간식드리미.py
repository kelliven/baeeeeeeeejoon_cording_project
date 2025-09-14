N=int(input())
line=list(map(int,input().split()))
stack=[]
order=1
for x in line:
    stack.append(x)
    while stack and stack[-1] == order:
        stack.pop()
        order+=1
if order == N+1: print("Nice")
else:print("Sad")