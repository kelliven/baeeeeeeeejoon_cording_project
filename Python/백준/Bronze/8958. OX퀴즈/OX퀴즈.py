test_case = int(input())
for i in range(test_case): #0~4회
    put_OX=list(str(input())) #0=OOXXOXXOOO, 1=OOXXOOXXOO...... i=...
    score=0
    plus=0
    for j in put_OX:
        if j=='O':
            score+=1
            plus+=score
        else:score=0
    print(plus)
