import sys;input=sys.stdin.readline
# 1
for _ in range(int(input())):
    num = int(input())
    for i in range(2,int(1e6)+1):
        if num % i == 0:
            print('NO'); break
    else:
        print('YES')

#2
mx = int(1e6)
check = [1]*(mx+1)
primes = []
for i in range(2,int(mx**0.5)+1):
    for j in range(2*i,mx+1,i):
        check[j] = 0
for i in range(2,mx+1):
    if check[i]:
        primes.append(i)

for _ in range(int(input())):
    num = int(input())
    for p in primes:
        if num % p == 0:
            print("NO")
            break
    else:
        print("YES")
