import sys, math
sys.stdin = open('testCase/1.txt', 'r')
input = sys.stdin.readline

n = int(input())
tree_list = list(map(int, [input() for _ in range(n)]))

# 각 원소의 차를 담은 리스트
diff_list = [tree_list[i+1] - tree_list[i] for i in range(n-1)]

# 모든 원소의 최대공약수를 구함
g = diff_list[0]
for i in diff_list[1:]:
    if i == 1:
        break;
    g = math.gcd(g, i)

# 최소수 = 간격 // 최대공약수 - 1
print(sum([x // g - 1 for x in diff_list]))