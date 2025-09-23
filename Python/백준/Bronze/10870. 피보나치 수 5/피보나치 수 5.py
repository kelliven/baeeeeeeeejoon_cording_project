def par(N):
    if N <= 1:
        return N
    return par(N-1)+par(N-2)
print(par(int(input())))