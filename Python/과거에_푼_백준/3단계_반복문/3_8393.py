#백준_8393

#풀이 1
n = int(input())
print(n*(n+1)//2)

#풀이 2
total = 0
for t in range(n+1):
    total = total + t
print(total)