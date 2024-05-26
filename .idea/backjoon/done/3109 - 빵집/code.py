import sys
sys.stdin = open('testCase/1.txt', 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10000)

r, c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]
move = [(-1, 1), (0, 1), (1, 1)] # 우상단, 우중단, 우하단 순서
ans = 0

def dfs(x, y):
    board[x][y] = 'x'
    if y == c-1:
        return True

    for a, b in move:
        dx, dy = x+a, y+b
        if dx >= r or dx < 0 or dy >= c or dy < 0 or board[dx][dy] == 'x':
            continue

        if dfs(dx, dy):
            return True
    return False

for i in range(r):
    if dfs(i, 0):
        ans += 1

print(ans)