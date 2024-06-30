import sys
sys.stdin = open('testCase/1.txt', 'r')
input = sys.stdin.readline

s = input().rstrip()
stack = []
for i in s:
    stack.append(i)
    if stack[-4:] == ['P', 'P', 'A', 'P']:
        for _ in range(3):
            stack.pop()

print("PPAP" if len(stack) == 1 and stack[-1] == "P" else "NP")