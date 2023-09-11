import sys; input = sys.stdin.readline

def f_r(x):
    if r_data[x]==0:
        return x
    res = f_r(r_data[x])
    r_data[x] = res
    return res

def union(a,b):
    ra, rb = f_r(a), f_r(b)
    if ra == rb: return
    if cost[ra] <= cost[rb]:
        r_data[rb] = ra
        cost[rb] = 0
    else:
        r_data[ra] = rb
        cost[ra] = 0

n,m,k = map(int,input().split())
r_data = [0]*(n+1)
cost = [0] + list(map(int,input().split()))

for _ in range(m):
    a, b = map(int,input().split())
    union(a,b)
ans = sum(cost)
print("Oh no") if ans > k else print(ans) 