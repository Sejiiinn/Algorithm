import sys
sys.stdin = open('../testCase/1267.txt', 'r')
input = sys.stdin.readline

input() # 첫줄 생략
y, m = 0, 0
for i in map(int,input().split()):
    y += (i // 30 + 1) * 10
    m += (i // 60 + 1) * 15

if y < m:
    print("Y %d" %y)
elif y > m:
    print("M %d" %m)
else:
    print("Y M %d" %y)