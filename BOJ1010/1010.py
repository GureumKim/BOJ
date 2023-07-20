import sys
input = sys.stdin.readline

def factorial(n):
    return n*factorial(n-1) if n>1 else 1

# 그냥 기본적인 조합 공식을 구현했다.
def combination(n,r):
    return factorial(n) / (factorial(r) * factorial(n-r))

T = int(input())
for tc in range(T):
    N, M = map(int, input().rstrip().split())
    result = combination(M,N)
    print(int(result))