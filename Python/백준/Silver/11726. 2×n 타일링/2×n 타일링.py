import sys
n=int(sys.stdin.readline())
if n==1:
    print(1)
    exit()
a,b=1,2
for _ in range(3,n+1):
    a,b=b,a+b
print(b%10007)