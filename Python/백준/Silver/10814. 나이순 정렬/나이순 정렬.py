import sys
input=sys.stdin.readline
N=int(input())
people=[]
for _ in range(N):
    age, name=input().split()
    people.append((int(age), name))
people.sort(key=lambda s:s[0])

out=[]
for age, name in people:
    out.append(f"{age} {name}\n")
sys.stdout.write(''.join(out))