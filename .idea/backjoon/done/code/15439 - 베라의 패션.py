import sys
sys.stdin = open('../testCase/15439.txt', 'r')
input = sys.stdin.readline

n = int(input())
print(n * (n-1))