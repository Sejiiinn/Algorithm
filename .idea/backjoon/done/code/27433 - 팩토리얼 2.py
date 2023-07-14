import sys
sys.stdin = open('../testCase/27433.txt', 'r')
input = sys.stdin.readline

def fac(num, n):
    if n == 0:
        print(num)
        return

    fac(num*n, n-1)

n = int(input())
fac(1, n)