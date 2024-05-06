import sys
sys.stdin = open('testCase/1.txt', 'r')
input = sys.stdin.readline

prime = [False]*2 + [True]*1000000

# 에라토스테네스의 체
for i in range(2, int(len(prime) ** 0.5)+1):
    prime[i*2::i] = [False]*len(prime[i*2::i])

for _ in range(int(input())):
    n = int(input())

    ans = 0
    for i in range(2, n//2+1):
        if prime[i] and prime[n-i]:
            ans += 1

    print(ans)