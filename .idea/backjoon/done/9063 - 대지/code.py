import sys
sys.stdin = open('/testCase/1.txt', 'r')
input = sys.stdin.readline

x,y = [],[]
for i in range(int(input())):
    a,b = map(int,input().split())
    x.append(a); y.append(b)
print((max(x)-min(x)) * (max(y)-min(y)))