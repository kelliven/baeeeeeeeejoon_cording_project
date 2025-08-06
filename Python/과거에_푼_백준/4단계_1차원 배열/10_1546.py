a=int(input())
num=list(map(int, input().split()))
max_num=max(num)
total=sum(num)
average=total/a
normalized=(average/max_num)*100
print(f"{normalized:.2f}")