import sys
sys.stdin = open('/testCase/1.txt', 'r')
input = sys.stdin.read

def cal(str, n):
    if n == 0:
        print(str)
        return

    cal(str + " "*len(str) + str, n-1)

for i in input().split():
    cal("-", int(i))