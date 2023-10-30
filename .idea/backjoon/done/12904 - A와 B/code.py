import sys
sys.stdin = open('testCase/1.txt', 'r')
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()
while len(t) > len(s):
    if t[-1] == "A":
        t = t[:-1]
    elif t[-1] == "B":
        t = t[:-1][::-1]
    else:
        print(0)
        break
else:
    print(1 if s == t else 0)