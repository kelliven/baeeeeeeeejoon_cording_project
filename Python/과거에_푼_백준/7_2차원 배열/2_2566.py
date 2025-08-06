b=[]
for _ in range(9):
    number=list(map(int,input().split()))
    b.append(number)
max_num=-1
max_y=0
max_x=0
for i in range(9):
    for j in range(9):
        if b[i][j] > max_num:
            max_num=b[i][j]
            max_y=i
            max_x=j
print(max_num)
print(max_y+1, max_x+1)