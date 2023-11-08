import sys
sys.stdin = open('testCase/1.txt', 'r')
input = sys.stdin.readline

lst = [list(map(int,input().split())) for i in range(int(input()))]
ans = float('inf')
for n in range(1, 1 << len(lst)): # 재료는 1가지 이상이므로 1부터 시작
    bit = list(map(int, bin(n)[2:].zfill(len(lst)))) # 자릿수를 맞추기 위해 zfill 사용
    total_a = 1
    total_b = 0
    for i in range(len(lst)):
        a, b = lst[i]
        if bit[i]:
            total_a *= a * bit[i]
        total_b += b * bit[i]
    ans = min(ans, abs(total_a - total_b))
print(ans)