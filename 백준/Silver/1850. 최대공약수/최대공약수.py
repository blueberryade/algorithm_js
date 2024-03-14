import sys
input = sys.stdin.readline

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

a,b = map(int,input().split())
result = gcd(a,b)
print('1'*result)