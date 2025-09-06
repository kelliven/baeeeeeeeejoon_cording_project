T=int(input())
sexy=""
for i in range(T):
    R,S=input().split()
    sex=list(S)
    for j in range(len(sex)):
        sexy+=sex[j]*int(R)
    print(sexy)
    sexy=""