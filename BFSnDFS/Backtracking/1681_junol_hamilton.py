def dfs(now=1,level=1,cost=0):
    global mn, flag
    if cost >= mn:
        return
    if level == n:
        if adj[now][1]:
            flag += 1
            mn = min(mn,cost+adj[now][1])
        return
    for i in range(1,n+1):
        if not visited[i] and adj[now][i]:
            visited[i] = 1
            dfs(i,level+1,cost+adj[now][i])
            visited[i] = 0

n = int(input())
adj = [[0]*(n+1)]+[[0]+list(map(int,input().split())) for _ in range(n)]
visited = [0]*(n+1)
visited[1] = 1
flag = 0
mn = 21e8
dfs()
print(mn) if flag else print(0)



# 백준 10971
from sys import stdin; input = stdin.readline
def hamilton(now,visit=1,cost=0):
    global ans
    if visit == n:
        if graph[now][i]:
            ans = min(ans,cost+graph[now][i])
        return
    for j in range(n):
        if not visited[j] and graph[now][j]:
            visited[j] = 1
            hamilton(j,visit+1,cost+graph[now][j])
            visited[j] = 0


n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [0]*n

ans = 21e8
for i in range(n):
    visited[i] = 1
    hamilton(i)
    visited[i] = 0
print(ans)

# DP로는 아래와 같다, nekote42님 풀이

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]


def find(visited, now):
    if (visited << N) | now in dp:
        return dp[(visited << N) | now]
    if visited == (1 << N) - 1:
        return cost[now][0] if cost[now][0] > 0 else 10 ** 9

    tmp = 10 ** 8
    for i in range(1, N):
        if not visited & (1 << i) and cost[now][i]:
            tmp = min(tmp, find(visited | (1 << i), i) + cost[now][i])

    dp[visited << N | now] = tmp
    return tmp


# key: visited << N | now, value: cost
dp = {}

# visited: bit로 표현된 방문한 도시 ex) 0b1000 4개 중 첫번째 도시만 방문함
print(find(1, 0))