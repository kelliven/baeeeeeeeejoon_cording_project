import sys
N=int(sys.stdin.readline())
text_set={sys.stdin.readline().strip('\n') for _ in range(N)}
m=sorted(text_set,key=lambda s:(len(s),s))
print(" ".join(m))