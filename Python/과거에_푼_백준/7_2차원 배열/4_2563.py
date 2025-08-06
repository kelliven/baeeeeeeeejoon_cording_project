paper=int(input())
space=[100*[0] for i in range(100)] # 도화지 크기요
for _ in range(paper): # 각각의 paper 넣기
    x, y=map(int,input().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
                space[i][j]=1
area=0
for sumit in space: #싹다 합치기
    area+=sum(sumit)
print(area)