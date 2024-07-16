import sys
sys.stdin = open('testCase/1.txt', 'r')
input = sys.stdin.readline

s = input().strip()
stack = []
for i in range(len(s)):
    # 여는 괄호일 경우 그냥 스택에 넣는다
    if s[i] == '(':
        stack.append(s[i])
    # 닫는 괄호일 경우 여는 괄호를 만날 때까지 순회하며 문자열의 길이를 센다.
    elif s[i] == ')':
        cnt = 0
        while True:
            cur = stack.pop()
            if cur == '(':
                break
            else:
                # cur은 1일 수도 있고, 압축을 해제한 문자열의 길이일 수도 있다.
                cnt += cur
        stack.append(stack.pop() * cnt)
    # 숫자이므로 문자열의 길이인 1을 스택에 넣는다. 단, 해당 숫자의 다음 문자열이 여는 괄호일 경우 곱셈을 하기 위해 그대로 넣어준다.
    else:
        stack.append(int(s[i]) if i+1 < len(s) and s[i+1] == '(' else 1)

print(sum(stack))