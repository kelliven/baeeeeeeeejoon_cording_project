import math
x1, y1, r1, x2, y2, r2=map(float, input().split())
d=math.sqrt((x2-x1)**2+(y2-y1)**2) #OK
if r1+r2<=d: #원 A,B이 서로 떨 어지거나 접하는 경우
    res=0 #영역 없음
    print("%.3f"%res)
elif abs(r2-r1)>=d: #원 A,B 중 하나가 안에 포함될 경우
    res=math.pi*(min(r1,r2)**2) #작은 원 넓이
    print("%.3f"%res)
else:
    angle_A=2*math.acos((r1**2+d**2-r2**2)/(2*r1*d)) # A 각도 계산
    angle_B=2*math.acos((r2**2+d**2-r1**2)/(2*r2*d)) # B 각도 계산
    
    c_A=(angle_A*r1**2)/2 # A 부채꼴 넓이
    c_B=(angle_B*r2**2)/2 # B 부채꼴 넓이
    
    s_A=(r1**2*math.sin(angle_A))/2 # A 삼각형 넓이
    s_B=(r2**2*math.sin(angle_B))/2 # B 삼각형 넓이

    res=(c_A-s_A)+(c_B-s_B) # (A 부채꼴 - A 삼각형) + (B부채꼴 - B 삼각형)
    print("%.3f"%res)