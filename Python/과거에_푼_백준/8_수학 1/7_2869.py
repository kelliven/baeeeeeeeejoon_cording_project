#높이 V
#이동거리 : 낮에는 A미터+ 밤에는 B미터-
#정상에는 멈춤
#정상까지 며칠?
# 1: A, B, V
A, B, V=map(int, input().split())
m=(V-B)//(A-B)
c=(V-B)%(A-B)
if c==0:
    print(m)
else: print(m+1)
    
    