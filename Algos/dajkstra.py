# Dijkstra algos

"""
최단 거리 구할 때 사용


(시작점 존재)
한 정점에서 다른 정점까지의 최단 거리

Dijkstra vs Belmanford
1. Dijkstra -> 음의 가중치 없다고 전제(음수 가중치 없음)
2. Belmanford -> 음의 가중치 존재할 수도


Floyd Warshell 문제
(얘는 시작점이 정해지지 않아도 됨, 시작점 fixed x)
모든 정점 -> 다른 모든 정점까지 치단 거리


음의 가중치 ==> 음의 사이클(무조건 작아지는 사이클 체크해주는 방법 필요하다)
"""

name = "ABCDE"
inf = int(21e8)
arr = [
    [0,3,inf,9,5],
    [inf,0,7,inf,1],
    [inf,inf,0,1,inf],
    [inf,inf,inf,0,inf],
    [inf,inf,1,inf,0]
]
used = [0]*5
used[0] = 1 #시작점은 경유지로 선택 안할 것
result = [0,3,inf,9,5] # 시작점 A에서 다른 모든 정점까지의 최소비용을 갱신 할 것임

def select_ky():
    Min = int(21e8)
    Minindex = 0
    for i in range(5):
        if used[i]==0 and result[i]<Min:
            Min=result[i]
            Minindex = i
    return Minindex

def dijkstra():
    # 경유지 선택
    for i in range(4):
        via = select_ky()   #ky = 경유지
        used[via] = 1
        # 시작점에서 도착점(시->도) vs 시 -> 경 -> 도 비교 후 최소비용을 result에 갱신
        for j in range(5):
            baro = result[j]    #  시 -> 도착점(바로)
            kyung = result[via]+arr[via][j] #시->경->도
            if baro>kyung:
                result[j] = kyung


dijkstra()
print(*result)

# 입력예제
# 5 7
# 0 1 3
# 0 4 5
# 0 3 9
# 1 4 1
# 1 2 7
# 2 3 1
# 4 2 1
# 0 3

import heapq
n, m = map(int,input().split())     # 정점의 개수 & 간선의 개수 입력
adj = [[] for _ in range(n)]        # 인접리스트 adj 선언

for _ in range(m):                  # 간선의 개수만큼 반복
    a, b, c = map(int,input().split())  # a 시작 b 도착, c 비용
    adj[a].append((b,c))
start, end = map(int,input().split()) # 시작점, 도착점 입력받기

inf = int(21e8)
result = [inf]*n

def dijkstra(start):
    heap = []   # 우선 순위 큐 이용시 사용될 리스트(인자값)
    heapq.heappush(heap,(0,0))   # 시작점을 경유지로 등록해주기 (sk 비용, 경유지 k), 비용을 기준으로 우선순위 따질 거니까
    result[start] = 0   # 시작점을 경유지로 놓았기 때문에 시=경, 비용을 0

    while heap:
        sk, k = heapq.heappop(heap) # sk(시작점에서 경유지까지 비용) k 선택한 경유지

        if sk > result[k]: continue

        for i in adj[k]: # 인접 행렬 내에서(경유지에서) 갈 수 있는 곳이 -> i (경유지 정보)
            cost = sk + i[1]    # 시 -> 경 + 경 -> 도착점 비용
            if cost < result[i[0]]: # 경유지 들렸을 때의 비용으로 갱신되는 조건
                result[i[0]] = cost # result 갱신
                heapq.heappush(heap,(cost,i[0]))


dijkstra(start)
print(*result)

# bfs vs dijkstra vs DP => 대기업 코테 ==> dihkstra or DP는 만점 bfs는 만점 x


## Floyd Warshall

inf = int(21e8)
arr = [
    [0,5,inf,8],
    [0,0,9,inf],
    [0,inf,0,4],
    [inf,inf,3,0]
]

for ky in range(4):        # 경유지
    for si in range(4):     # 시작점
        for do in range(4): # 도착점

            if arr[si][do] > arr[si][ky]+arr[ky][do]:
                arr[si][do] = arr[si][ky] + arr[ky][do]

for i in range(4):
    for j in range(4):
        print(arr[i][j],end=' ')
    print()
