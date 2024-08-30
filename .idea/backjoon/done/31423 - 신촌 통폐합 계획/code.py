import sys
sys.stdin = open('testCase/1.txt', 'r')
input = sys.stdin.readline

n = int(input())
colleges = [""] + [input().rstrip() for _ in range(n)]
next = [-1] * (n+1)
tail = [i for i in range(n+1)]

for _ in range(n-1):
    x, y = map(int, input().split())
    next[tail[x]] = y
    tail[x] = tail[y]

result = []
for _ in range(n):
    result += colleges[x]
    x = next[x]
print("".join(result))