n = int(input())
for i in range(2,int(n**0.5)+1):
    while not n%i:
        print(i)
        n //= i # 소수로 끝까지 나뉘게 된다.
    if n == 1: break # 2이상인 n은 결국 1이되게 됨 이 때 break

# 아래는 메모리 초과
# 문제를 잘 읽고 조건을 확실히 파악한 다음
# 어디서부터 어디까지 필요한지를 확실히 파악하고 문제를 풀자

def eratos(n):
    for i in range(2,int(n**0.5)+1):
        for j in range(2*i,n+1,i):
            primes[j] = 0
def p_factor(n):
    for i in range(2,n+1):
        if primes[i]:
            for j in range(1,n+1):
                temp = i*j
                if temp > n:break
                cnt = 0
                while not temp%i and temp>1:
                    cnt+=1
                    temp//=i
                factors[i*j] += [i]*cnt
n = int(input())
primes = [0,0] + [1]*(n-1)
factors = [[] for _ in range(n+1)]
eratos(n)
p_factor(n)

for p in factors[n]:
    print(p)

