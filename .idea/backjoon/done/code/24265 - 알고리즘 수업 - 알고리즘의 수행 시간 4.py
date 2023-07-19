import sys
sys.stdin = open('../testCase/24264.txt', 'r')
input = sys.stdin.readline

n = int(input())
print(n*(n-1)//2)
print(2)