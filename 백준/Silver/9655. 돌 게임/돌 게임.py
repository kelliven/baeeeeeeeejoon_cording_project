N=int(input())
#SK,CY
#1 SK 상1
#2 CY 상1 창1
#3 SK 상3
#4 CY 상1 창3, 상3 창1, 상1 창1 상1 창1
#5 SK 상1 창1 상1 창1 상1, 상1 창3 상1, 상3 창1 상1, 상3 창1 상1
#6 CY ...
#7 SK ...
if N%2==0:
    print('CY')
else:print('SK')