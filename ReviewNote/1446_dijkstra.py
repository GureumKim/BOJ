import heapq as hq
import sys; input = sys.stdin.readline

def dijkstra(start=0):
    heap = []
    hq.heappush(heap,(0,0))
    result[start] = 0

    while heap:
        v_cost, via = hq.heappop(heap)

        if v_cost > result[via]: continue #무방향 x, visited배엺은 필요x

        for next, cost in data[via]:
            cost += v_cost
            if cost < result[next]:
                result[next] = cost
                hq.heappush(heap,(cost,next))

            
n, d = map(int,input().split())

data = [[] for _ in range(d+1)]
for _ in range(n):
    s,e,c = map(int,input().split())
    if e > d: continue
    data[s].append((e,c))

mx = 10000
result = [mx]*(d+1)

###
# 일단 지름길 아니면 1의 거리로 다음 노드로 연결되어 있는 조건!!!!!!
###
for i in range(d):
    data[i].append((i+1,1))

dijkstra()
print(result[d])
