import sys; input = sys.stdin.readline
from math import sqrt
n = int(input())
primes = [0]*(n+1)
for i in range(2,int(sqrt(n))+1):
    for k in range(i+i,n+1,i):
        if primes[k]: continue
        primes[k] = 1
l = 2; h = 3
cnt = 1
s = l + h
while h <= n/2 or l!=h: # INDEXErorr 조심 n==1혹은 최대값일 때!!
    if s == n:
        cnt += 1
    elif s < n:
        h += 1
    else:
        l += 1
print(cnt)

