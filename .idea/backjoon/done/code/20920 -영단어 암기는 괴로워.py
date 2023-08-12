import sys
sys.stdin = open('../testCase/20920.txt', 'r')
input = sys.stdin.readline

n,m = map(int,input().split())
dict = dict()

for _ in range(n):
    s = input().rstrip()
    if dict.get(s):
        dict[s] += 1
    elif len(s) >= m:
        dict[s] = 1
for a, b in sorted(dict.items(), key=lambda x:(-x[1], -len(x[0]), x[0])):
    print(a)