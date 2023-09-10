import sys
sys.stdin = open('../testCase/26069.txt', 'r')
input = sys.stdin.readline

dance = set(["ChongChong"])
for _ in range(int(input())):
    a,b = input().split()
    if a in dance or b in dance:
        dance.add(a)
        dance.add(b)
print(len(dance))