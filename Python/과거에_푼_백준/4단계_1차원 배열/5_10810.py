N, M = map(int, input().split())
o=[]
for a in range(N): #5번 0~4
    o.append(0)
for b in range(M): #4번 0~3
    i, j, k = map(int, input().split())
    for c in range(i-1, j):
        o[c]=k
print(" ".join(map(str, o)))



