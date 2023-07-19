import sys
sys.stdin = open('../testCase/24264.txt', 'r')
input = sys.stdin.readline

print(sum([i for i in range(int(input()))]))
print(2)