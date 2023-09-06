import sys;input = sys.stdin.readline
a,b = map(int,input().split())
primes = [0,0]+[1]*(b-1)
n_factors = [0,0]+[1]*(b-1)

# 에라토스
for i in range(2,int(b**0.5)+1):
    for j in range(2*i,b+1,i):
        primes[j] = n_factors[j] = 0

for i in range(2,b+1):
    for j in range(2,b+1):
        if i*j > b: break
        if primes[j]:
            n_factors[i*j] = n_factors[i]+1
ans = 0
for i in range(a,b+1):
    if primes[n_factors[i]]:
        ans += 1
print(ans)