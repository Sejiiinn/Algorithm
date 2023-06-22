import sys
sys.stdin = open('../testCase/4344.txt', 'r')
input = sys.stdin.readline

def roundTraditional(val, digits):
    return round(val+10**(-len(str(val))-1), digits)

a = int(input())
for i in range(a):
    b = list(map(int,input().split()))
    c = (sum(b)-b[0])/b[0]
    d = 0
    for j in range(1,len(b)):
        if b[j]>c:
            d += 1
    print("%.3f%%" % roundTraditional(d/b[0]*100, 3))