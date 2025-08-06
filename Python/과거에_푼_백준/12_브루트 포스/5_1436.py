N=int(input())
x, y=0, 0
while True:
    x+=1
    if "666" in str(x):
        y+=1
        if y == N:
            print(x)
            break
