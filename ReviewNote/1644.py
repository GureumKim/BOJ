# 시간 더 줄여보기!
# 일단 순서대로 가는 게 오래 걸리면 거꾸로 가는 것도 생각해보기!

import sys; input = sys.stdin.readline
n = int(input())
primes = [0,0]+[1]*(n-1)
for i in range(2,int(n**0.5)+1):
    for k in range(i+i,n+1,i):
        primes[k] = 0

ans = 1 if primes[n] else 0
s=e= n-1
pre = []
temp = n-1
while 2<=s:
    if temp == n:
        ans += 1
    if temp<=n:
        s-=1
        while not primes[s]:
            s-=1
        pre.append(s)
        temp += s
    else:
        temp -= e
        e=pre.pop(0)
print(ans)
    
    