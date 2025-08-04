N=int(input()) # input = 13, output = 3
x=0
a=1
while N>=a:
    a+=6*x
    x+=1
    if N==a:break
print(x)