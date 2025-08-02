B, N = input().split()
N=int(N) # ex) 36 진법
num=len(B) #ex) ZZZZZ = 5개
alyphabet=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J",
           "K","L","M","N","O","P","Q","R","S","T",
           "U","V","W","X","Y","Z"]
# ZZZZZ=35*36^0 + 35*36^1 + 35*36^2 + 35*36^3 + 35*36^4
#[0,1,2,3,5]의 Z를 뽑고 35씩 뽑음.
#뽑은 각 Z에 진법 변환 곱셈
summit=1
final_multi_list=[]
multipli=0
for i in range(num): #0,1,2,3,4
    for j in alyphabet:
        #print("test : %s"%(B[i])) 통과
        if B[i] == j:
            alyphabet_number=alyphabet.index(j)
            multipli=alyphabet_number # 알파벳의 10진법 나옴 ex) z=35
            final_multi_list.append(multipli) #알파벳 갯수만큼 나옴 EX) 35, 35, 35, 35, 35

final_value = 0
for r in range(num):
    exponent = num - r - 1 #역순 -> 4, 3, 2, 1
    summit = N ** exponent  #역순의 36^... 거듭제곱
    value = final_multi_list[r]*summit
    final_value+=value
    
print(final_value)