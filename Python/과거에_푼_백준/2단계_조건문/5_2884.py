H, M = map(int, input().split())
if 45<=M<60:
        print("%d %d"%(H, M-45))
elif 0<=M<45:
    if H==0:
        print("23 %d"%(M+15))
    elif 23>H-1>=0: print("%d %d"%(H-1, M+15))