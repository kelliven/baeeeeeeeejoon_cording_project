abc_list=[]
for k in range(5):
    put_str=str(input())
    abc_list.append(put_str)
result=""
high=max(len(word) for word in abc_list)
for j in range(high):
    for i in range(len(abc_list)):
        if j < len(abc_list[i]):
            result+=abc_list[i][j]
print(result)



