import sys
sys.stdin = open('/testCase/1.txt', 'r')
input = sys.stdin.readline

n = int(input())
print('%d\n%d' %(n**3, 3))