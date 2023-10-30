import sys
sys.stdin = open('/testCase/1.txt', 'r')
input = sys.stdin.readline

n = int(input())
a = input().rstrip()
b = input().rstrip()
if n % 2 == 0:
    print("Deletion succeeded" if a == b else "Deletion failed")
else:
    for i in range(len(a)):
        if a[i] == b[i]:
            print("Deletion failed")
            break
    else:
        print("Deletion succeeded")