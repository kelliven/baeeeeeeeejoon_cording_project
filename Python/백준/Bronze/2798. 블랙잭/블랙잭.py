N,M=map(int,input().split())
card_jack=list(map(int,input().split()))
sum_list=[]
for i in card_jack:
    for j in card_jack:
        for k in card_jack:
            if i!=j and j!=k and k!=i:
                sum=i+j+k
                if sum<=M:
                    sum_list.append(sum)
print(max(sum_list))