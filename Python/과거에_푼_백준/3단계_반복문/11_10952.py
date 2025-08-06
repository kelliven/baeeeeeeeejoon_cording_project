C=[]
a=1
while a==1:
    A,B=map(int, input().split())
    if A==0 and B==0:
        break
    else:C.append((A,B))
for i in range(len(C)):
    result=C[i][0]+C[i][1]
    print(result)