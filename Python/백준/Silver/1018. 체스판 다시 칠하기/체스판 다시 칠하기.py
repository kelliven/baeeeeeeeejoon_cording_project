#y,x 보드를 만든다.
#검사할 좌표를 찍는다.
#그 좌표를 기반으로 8x8을 검사한다.
N,M=map(int, input().split()) #y,x축
board = [input() for _ in range(N)]  # M개의 문자열
def repaint_cost(yi, xi):
    repair_cost_B=0
    for i in range(8):
        for j in range(8):
            if (i+j)%2==0:
                expected='B'
            else:expected='W'
            if board[yi+i][xi+j]!=expected:
                repair_cost_B+=1
    repair_cost_W=64-repair_cost_B
    return min(repair_cost_B, repair_cost_W)
#검사시작할 좌표 지정하기.
ans=64
for yi in range(N-7):
    for xi in range(M-7):
        anser=repaint_cost(yi,xi)
        ans=min(ans,anser)
print(ans)