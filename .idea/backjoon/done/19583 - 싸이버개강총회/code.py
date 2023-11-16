import sys
sys.stdin = open('testCase/1.txt', 'r')
input = sys.stdin.read

def get_minute(text):
    h, m = list(map(int, text.split(":")))
    return h*60 + m

text = input().strip().split("\n")
s, e, q = map(get_minute, text[0].split())

ans = 0
hashSet = set()
for chat in text[1:]:
    t, id = chat.split()
    t = get_minute(t)

    if t > q:
        continue

    # 입장
    if t <= s:
        hashSet.add(id)
        continue

    # 퇴장
    if e <= t and id in hashSet:
        hashSet.remove(id)
        ans += 1

print(ans)