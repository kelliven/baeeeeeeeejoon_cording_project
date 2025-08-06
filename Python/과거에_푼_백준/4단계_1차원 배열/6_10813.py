N, M= map(int, input().split())
o=[i for i in range(1, N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    o[i-1], o[j-1] = o[j-1], o[i-1]
print(" ".join(map(str, o)))
    



