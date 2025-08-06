X=[]
for i in range(9):
    N=int(input())
    X.append(N)
    num_max=max(X)
    if num_max==X[i]:
        a=i+1
print(num_max)
print(a)
