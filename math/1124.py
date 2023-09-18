import sys;input=sys.stdin.readline
a,b = map(int,input().split())
primes = [0,0] + [1]*(b-1)
for i in range(2,int((b**(1/2)))+1):
    for j in range(2*i,b+1,i):
        primes[j] = 0
ans = 0
for i in range(a,b+1):
    cnt = 0
    for p in range(2,i):
        if primes[p]:
            temp = i
            while temp%p==0:
                cnt += 1
                temp//=p
    if primes[cnt]:
        ans += 1
print(ans)