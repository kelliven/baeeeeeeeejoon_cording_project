a, b=map(int,input().split())
a0,b0=a,b
num=[]
i=2
c=1
while i<=min(a,b):
    if a%i==0 and b%i==0:
        a//=i
        b//=i
        c*=i
    else:
        i+=1
print(c)
print((a0*b0)//c)