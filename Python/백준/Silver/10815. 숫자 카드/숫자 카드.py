N=int(input())
N_list=set(list(map(int,input().split())))
C=int(input())
c_list=list(map(int,input().split()))
for i in c_list:
    if i in N_list:
        print(1,end=" ")
    else: print(0,end=" ")