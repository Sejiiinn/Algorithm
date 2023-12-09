# https://school.programmers.co.kr/learn/courses/30/lessons/250136

def solution(land):
    n, m = len(land), len(land[0])
    direction = [(0,1), (1,0), (0,-1), (-1,0)]
    visited = [[False]*m for _ in range(n)]
    num = 2 # 석유 덩어리에 붙여줄 번호
    size_dict = dict()

    # land 를 순회하며 덩어리에 번호를 붙이고 사이즈를 측정
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                # BFS
                q = [(i, j)]
                visited[i][j] = True
                size = 0

                while q:
                    x, y = q.pop()
                    land[x][y] = num
                    size += 1
                    for a, b in direction:
                        dx, dy = x+a, y+b
                        if n > dx >= 0 and m > dy >= 0 and land[dx][dy] == 1 and not visited[dx][dy]:
                            visited[dx][dy] = True
                            q.append((dx, dy))

                size_dict[num] = size
                num += 1

    # 시추
    ans = 0
    for i in range(m):
        cand = set()
        for j in range(n):
            if land[j][i] != 0:
                cand.add(land[j][i])
        ans = max(ans, sum([size_dict[x] for x in cand]))
    return ans
