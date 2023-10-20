from itertools import combinations
from collections import deque

def check(group):
    if len(group) == 1:
        return True
    q = deque()
    q.append(group[0])
    visited = [0] * (n + 1)

    while q:
        now = q.popleft()
        for next_node in adj[now]:
            if visited[next_node] == 0 and next_node in group:
                visited[next_node] = 1
                q.append(next_node)
    for idx in group:
        if visited[idx] == 0:
            return False
    return True

def get_pops(group):
    pops = 0
    for i in group:
        pops += populations[i]
    return pops

n = int(input())
populations = [0] + list(map(int, input().split()))
adj = [[]]

for _ in range(n):
    adj.append(list(map(int, input().split()))[1:])

lst = set(range(1, n + 1))
mn = float('inf')
for i in range(1, n):
    for group1 in combinations(lst, i // 2 + 1):
        group2 = tuple(lst.difference(set(group1)))
        res1, res2 = check(group1), check(group2)
        if res1 and res2:
            mn = min(mn, abs(get_pops(group1) - get_pops(group2)))
print(-1 if mn == float('inf') else mn)


# def dfs(start=0,sum=0):
#     # print(sum)
#     if sum > n:
#         return 0
#     if sum == n and sum != 0:
#         return 1
    
#     for i in range(start,len(facto)):
#         flag = dfs(i+1,sum+facto[i])
#         if flag: return 1

# facto = [1, 1]
# i = 1
# while facto[i] <= int(1e18):
#     facto.append(facto[i]*(i+1))
#     i +=1
# # print(facto)
# n = int(input())

# ans = dfs()
# print('YES' if ans else 'NO')



# # 참고

# def fac(n):
#     if n == 0:
#         return 1
#     fac = 1
#     for i in range(1,n+1):
#         fac *= i
#     return fac

# n = int(input())
# if n == 0:
#     print("NO")
#     exit()

# for i in range(20, -1, -1):
#     if n>=fac(i):
#         n -= fac(i)
# if n == 0:
#     print("YES")
# else:
#     print("NO")


