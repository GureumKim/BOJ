from collections import deque
from sys import stdin; input = stdin.readline
def bfs():
    q = deque()
    q.append((1,0))
    visited[1] = 1
    while q:
        now,dist=q.popleft()
        for next in adj[now]:
            if visited[next]: continue
            visited[next] = 1 
            q.append((next,dist+1))
            distance[dist+1].append(next)
    return dist

n, m = map(int,input().split())
adj = [[] for _ in range(n+1)]
distance = [[] for _ in range(n) ]
visited = [0]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

mx = bfs()
distance[mx].sort()
print(distance[mx][0], mx, len(distance[mx]))