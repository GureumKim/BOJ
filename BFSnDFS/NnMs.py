import sys; input=sys.stdin.readline

# 15649

def dfs(level=0):
    if level == m:
        print(*sequence)
        return
    for i in range(1,n+1):
        if visited[i]:continue
        visited[i] = 1
        sequence[level] = i
        dfs(level+1)
        visited[i] = 0
    
n,m = map(int,input().split())
sequence = [0]*m
visited = [0]*(n+1)
dfs()
