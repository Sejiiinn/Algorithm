import sys
sys.stdin = open('testCase/1.txt', 'r')
input = sys.stdin.readline

for i in range(int(input())):
    print("%d. %s" %(i+1, input().rstrip()))