# https://school.programmers.co.kr/learn/courses/30/lessons/178871

def solution(players, callings):
    rank = dict()
    for i in range(len(players)):
        rank[players[i]] = i

    for name in callings:
        idx = rank[name]
        # 인덱스 변경
        rank[players[idx-1]], rank[name] = rank[name], rank[players[idx-1]]

        # 실제 위치 변경
        players[idx], players[idx-1], = players[idx-1], players[idx]

    return players