import sys
input=sys.stdin.readline
N=int(input())
N_card=list(map(int,input().split()))
M=int(input())
M_card=list(map(int,input().split()))
count_card={}
for num in N_card:
    if num in count_card:
        count_card[num]+=1
    else:count_card[num]=1
result=[]
for num in M_card:
    result.append(count_card.get(num,0))
print(' '.join(map(str,result)))