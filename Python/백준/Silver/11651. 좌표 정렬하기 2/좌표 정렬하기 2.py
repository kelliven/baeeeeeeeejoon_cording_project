import sys
input=sys.stdin.readline
n=int(input())
array=[]
for i in range(n):
    [a,b]=map(int,input().split())
    array.append([b,a])
s_array = sorted(array)
for i in range(n):
    print(s_array[i][1],s_array[i][0])