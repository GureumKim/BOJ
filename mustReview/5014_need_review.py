import sys;input=sys.stdin.readline
from collections import deque 
def bfs(start):     #최소!!
    q = deque([start])
    visited[start] = 1  # 자기 자신일 때 아무것도 누르지 않음
    while q:
        now = q.popleft()
        if now == G:
            return visited[now]-1   # 자기 자신일 때 아무것도 누르지 않음
        for go in (now+U,now-D):
            if 0<go<=F and not visited[go]:
                visited[go] = visited[now]+1
                q.append(go)
    return "use the stairs"



F,S,G,U,D = map(int,input().split())
visited = [0]*(F+1)
print(bfs(S))