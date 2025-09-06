while True:
    t_s=sorted(map(int,input().split()))
    if t_s!=[0,0,0]:
        if t_s[2]**2==t_s[0]**2+t_s[1]**2:
            print("right")
        else:print("wrong")
    else:break