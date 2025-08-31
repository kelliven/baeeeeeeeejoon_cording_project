from collections import Counter
import sys
N=int(sys.stdin.readline()) #입력 값은 홀수.
sum=0
a=[]
for i in range(N):
    x=int(sys.stdin.readline())
    sum+=x
    a.append(x)
srtd=sorted(a)
Get=Counter(srtd).most_common(2)
#산술평균 : N개의 수들의 합을 N으로 나눈 값
print(round(sum/N))
#중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
print(srtd[len(a)//2])
#최빈값 : N개의 수들 중 가장 많이 나타나는 값
if len(a)>1:
    if Get[0][1]==Get[1][1]:
        print(Get[1][0])
    else:print(Get[0][0])
else:print(Get[0][0])    
#범위 : N개의 수들 중 최댓값과 최솟값의 차이
print(max(a)-min(a))