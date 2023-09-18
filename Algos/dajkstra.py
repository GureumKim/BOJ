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