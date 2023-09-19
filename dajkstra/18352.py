from sys import stdin;input=stdin.readline
import heapq as hq

def dajkstra(start):
    heap = []
    hq.heappush(heap,(0,start))
    result[start] = 0
    while heap:
        v_cost,via = hq.heappop(heap)

        if v_cost > result[via]: continue

        for i in adj[via]:
            cost = v_cost + 1
            if cost < result[i-1]:
                result[i] = cost
                hq.heappush(heap,(cost,i))


n, m, k, x = map(int,input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    s, e = map(int,input().split())
    adj[s].append(e)

inf = int(21e8)
result = [inf]*n

dajkstra(x)

flag = 0
for i in range(n):
    if result[i] == k:
        flag = 1
        print(i+1)
if not flag:
    print(-1)
