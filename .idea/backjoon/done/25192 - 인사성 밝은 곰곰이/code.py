import sys
sys.stdin = open('/testCase/1.txt', 'r')
input = sys.stdin.readline

entered = set()
cnt = 0
for _ in range(int(input())):
    s = input().strip()
    # 엔터가 존재하면 목록 초기화
    if s == "ENTER":
        entered.clear()
        continue

    # 이미 인사를 했다면 넘김
    if s in entered:
        continue
    # 새 채팅이므로 목록에 추가하고 인사 횟수 +1
    else:
        cnt += 1
        entered.add(s)
print(cnt)