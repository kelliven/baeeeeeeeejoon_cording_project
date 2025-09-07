from collections import Counter
A=int(input())
B=int(input())
C=int(input())
c=Counter(str(A*B*C))
for i in range(10):
    if str(i) in c:
        print(c[str(i)])
    else:print('0')