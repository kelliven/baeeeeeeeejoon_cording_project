N, X=map(int, input().split())
A=list(map(int, input().split()))
num=list()
for i in A:
    if i<X:
        num.append(i)
print(" ".join(map(str, num)))