import sys
input = sys.stdin.readline

k = 10**9+7

def mod(a,b):
    a %= k
    if b==0:
        return 1
    
    x= mod(a,b//2)
    x*=x
    x%=k

    if b%2==1:
        x=x*a
        x%=k
    
    return x

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(mod(a, b))