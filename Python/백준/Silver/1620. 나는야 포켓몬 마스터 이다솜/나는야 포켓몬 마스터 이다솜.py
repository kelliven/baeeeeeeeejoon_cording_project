import sys
N,M=map(int,sys.stdin.readline().split())
str_list={}
num_list={}
for i in range(1,N+1):
    name=sys.stdin.readline().strip()
    str_list[i]=name
    num_list[name]=i
for _ in range(M):
    input_M=sys.stdin.readline().strip()
    if input_M in num_list:print(num_list[input_M]) #문자열 입력 시
    else: print(str_list[int(input_M)]) #숫자형 입력 시