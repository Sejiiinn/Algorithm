import sys
sys.stdin = open('/testCase/1.txt', 'r')
input = sys.stdin.readline

n = input()
arr = list(map(int, input().split()))[::-1]
stack = []
goal = [0]
while arr or stack:
    if arr and arr[-1] == goal[-1] + 1:
        goal.append(arr.pop())
        continue

    if stack and stack[-1] == goal[-1] + 1:
        goal.append(stack.pop())
        continue

    if arr:
        stack.append(arr.pop())
    else:
        print("Sad")
        break
else:
    print("Nice")
