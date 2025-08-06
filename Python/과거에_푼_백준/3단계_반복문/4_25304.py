#입력
#1: 영수증) 금액 X
#2: 영수증) 구매한 물건 종류의 수 N
#n: 각 물건 가격 a, 개수 b
#출력
# a*b==X*N 이면 YES출력 아니면 NO

X=int(input())
N=int(input())
d=0
for _ in range(N):
   a, b=map(int,input().split())
   d+=a*b
if d==X:print("Yes")
else:print("No")
