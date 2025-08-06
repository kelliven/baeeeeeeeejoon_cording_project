x=[]
y=[]
z=[]
w=[]
for i in range(20):
    num=list(map(str, input().split()))
    x.append(num)
for j in range(20):
    y.append(int(float(x[j][1]))) #y는 수업 학점
    z.append(x[j][2])
for k in range(20): #z는 시험 점수
    if z[k]=='A+':z[k]=4.5
    elif z[k]=='A0':z[k]=4.0
    elif z[k]=='B+':z[k]=3.5
    elif z[k]=='B0':z[k]=3.0
    elif z[k]=='C+':z[k]=2.5
    elif z[k]=='C0':z[k]=2.0
    elif z[k]=='D+':z[k]=1.5
    elif z[k]=='D0':z[k]=1.0
    elif z[k]=='F':z[k]=0
    elif z[k]=='P':z[k]='P'
    else: z[k]=0
score=0
credit=0
for q in range(20):
    if z[q]=='P':
        continue
    score+=z[q]*y[q]
    credit+=y[q]
if score!=0:
    total_score=score/credit
    print(f"{total_score:.6f}")
else: print("0.000000")