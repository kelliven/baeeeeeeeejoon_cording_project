from string import ascii_lowercase
alpha=list(ascii_lowercase)
List=[]
A=list(str(input()))
for i in range(len(alpha)):
    if alpha[i] in A:
        print(A.index(alpha[i]),end=" ")
    else:
        print(-1,end=" ")