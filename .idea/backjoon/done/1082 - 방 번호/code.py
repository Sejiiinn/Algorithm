import sys
sys.stdin = open('testCase/1.txt', 'r')
input = sys.stdin.readline

n = int(input())
costs = list(map(int, input().split()))
m = int(input())
dp = [-1]*(m+1)
# 숫자를 내림차순으로 순회
for num in range(n-1, -1, -1):
    # 현재 숫자의 cost 부터 최대 가격까지 순회
    for cost in range(costs[num], m+1):
        dp[cost] = max(num, dp[cost], dp[cost-costs[num]]*10 + num)
print(dp[-1])
