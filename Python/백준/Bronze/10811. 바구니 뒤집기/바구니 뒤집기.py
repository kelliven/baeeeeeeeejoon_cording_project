N,M=map(int,input().split())
A=0
B=[i+1 for i in range(N)]
for q in range(M):
    i,j=map(int,input().split())
    B[i-1:j]=B[i-1:j][::-1]
print(' '.join(map(str,B)))