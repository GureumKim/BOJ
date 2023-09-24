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