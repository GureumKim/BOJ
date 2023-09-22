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


"""
이 유형 요렇게도 가능 
ex. SWEA 1238.
"""
# contact, 숨바꼭질 유형
# 중간 중간에 비어있는 번호가 있을 수 있다 => sparse 그래프 될 수 있음 ==> 인접 리스트 써라(인접행렬 nono)
# 항상 다자 간 통화를 통해 동시에 전달(우선 순위x, 걍 나중에 마지막 연락 중 가장 마지막 번호를 출력만
from collections import deque
def bfs(start):
    visited = [0]*101
    q = deque()
    q.append(start)
    visited[start] = 1

    max_number = start
    max_depth = 1

    while q:
        now = q.popleft()
        for to in adj[now]:
            if visited[to]:continue
            visited[to] = visited[now]+1
            if max_depth<visited[to] or (max_depth==visited[to] and max_number < to):
                max_depth = visited[to]
                max_number = to
            q.append(to)
    return max_depth, max_number
    # return visited[now]

for tc in range(1,11):
    n, start = map(int,input().split())
    data = list(map(int,input().split()))

    adj = [[] for _ in range(101)]
    # visited = [0] * 101
    for i in range(0,n,2):
        # from_,to_ = data[i],data[i+1]
        adj[data[i]].append(data[i+1])
    print(*bfs(start))
    # mx_dist = bfs(start)
    # ans = []
    # for i in range(101):
    #     if visited[i] == mx_dist:
    #         ans.append(i)
    # print(f"#{tc} {ans[-1]}")