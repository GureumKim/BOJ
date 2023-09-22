from sys import stdin; input = stdin.readline
import heapq as hq

def dijkstra(start):
    heap = []
    hq.heappush(heap,(0,start)) # t from 0 , start node
    result[start] = 0

    while heap:
        tt, via = hq.heappop(heap)

        if tt > result[via]: continue

        for next,till_infected in adj[via]:
            till_infected += tt
            if till_infected < result[next]:
                result[next] = till_infected
                hq.heappush(heap,(till_infected,next))

for _ in range(int(input())):
    n, d, c = map(int,input().split())
    adj = [[] for _ in range(n+1)]

    for _ in range(d):
        a, b, k = map(int,input().split())
        adj[b].append((a,k))
    inf = int(21e8)
    result = [inf]*(n+1)

    dijkstra(c)

    amt = t = 0
    for i in range(1,n+1):
        if result[i] != inf:
            amt +=1
            t = max(t,result[i])
    print(amt, t)