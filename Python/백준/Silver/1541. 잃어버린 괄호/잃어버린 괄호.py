put=input()
minus=put.split('-')
result=sum(map(int,minus[0].split('+')))
for minu in minus[1:]:
    result-=sum(map(int,minu.split('+')))
print(result)