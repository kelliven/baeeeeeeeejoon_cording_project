N,M=map(int,input().split())
A=[]
B=[]
for _ in range(N):
    x=list(map(int, input().split()))
    A.append(x)
for _ in range(N):
    y=list(map(int, input().split()))
    B.append(y)
for i in range(N):
    sum_C=[A[i][j]+B[i][j] for j in range(M)]
    print(" ".join(map(str,sum_C)))
    #isdigit() : 문자에 숫자만 있나? 판별 메서드
    #isalpha() : 문자가 전부 알파벳인가? 판별 메서드