Test=int(input())
for _ in range(Test):
    fiboNum=int(input())
    a,b=1,0
    for _ in range(fiboNum):
       a,b=b,a+b
    print(a,b)