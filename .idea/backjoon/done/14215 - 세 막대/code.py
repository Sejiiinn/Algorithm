import sys
sys.stdin = open('/testCase/1.txt', 'r')
input = sys.stdin.readline

a,b,c = map(int,input().split())
arr = [a,b,c]
max_num = max(arr)
arr.remove(max_num)
print(sum(arr)+max_num if max_num < sum(arr) else sum(arr)*2-1)