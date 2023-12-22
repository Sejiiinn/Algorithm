import sys
sys.stdin = open('testCase/1.txt', 'r')
input = sys.stdin.readline

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for _ in range(int(input())):
    n = int(input())
    while True:
        if isPrime(n):
            print(n)
            break

        n+=1