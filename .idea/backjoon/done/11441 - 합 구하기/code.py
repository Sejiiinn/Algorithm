import sys
sys.stdin = open('/testCase/1.txt', 'r')
input = sys.stdin.readline

n = int(input())
lst = [0]
for i in map(int,input().split()):
    lst.append(lst[-1] + i)
for _ in range(int(input())):
    a, b = map(int,input().split())
    print(lst[b] - lst[a-1])