import sys
N, M=map(int,sys.stdin.readline().split())
N_list=set(sys.stdin.readline().strip() for _ in range(N))
M_list=set(sys.stdin.readline().strip() for _ in range(M))
a=sorted(N_list&M_list)
print(len(a))
print("\n".join(a))