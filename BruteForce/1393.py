from math import sqrt
def bruteforce(ex,ey):
    global mn,mx,my
    # 최소거리 : 피타고라스 정리 이용
    temp = sqrt(abs(ex-sx)**2+abs(ey-sy)**2)
    # 한 방향으로만 가므로 dx,dy가 0,0인 경우 부등호로 해결
    # 그 이외의 경우는 같은 거리 안나오니까 커지게 될 때 return
    if temp >=mn:
        return
    if mn > temp:
        mn = temp
        mx,my = ex,ey
    bruteforce(ex+dx,ey+dy)

# 재귀로 최대 공약수 구하기
def gcd(x,y):
    while y:
        return gcd(y,x%y)
    return  x

sx,sy = map(int,input().split())
ex,ey,dx,dy = map(int,input().split())
g = gcd(abs(dx),abs(dy))
dx,dy = dx//g,dy//g

mn = 21e8
mx,my = 0,0
bruteforce(ex,ey)
print(mx,my)


# 1837
def check():
    for i in range(2,k):
        if primes[i] and p%i==0:
            return i
    return 1

primes = [0,0]+[1]*int(1e6-1)
for i in range(2,int(1e6**0.5)+1):
    for j in range(2*i,int(1e6+1),i):
        primes[j] = 0
p, k = map(int,input().split())
ans = check()
print('GOOD') if ans == 1 else print('BAD', ans)