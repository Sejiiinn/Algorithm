import sys
sys.stdin = open('/testCase/1.txt', 'r')
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))

ans = [b[i] for i in range(n) if not a[i]*b[i]][::-1]
ans += [c[i] for i in range(m - len(ans))]
print(*ans[:m])