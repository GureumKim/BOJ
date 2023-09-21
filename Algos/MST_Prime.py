#https://www.geeksforgeeks.org/difference-between-prims-and-kruskals-algorithm-for-mst/

"""
하나의 정점에서 연결된 간선들 중에서 하나씩 선택해서
MST를 만들어 가는 방식

1) 임의 정점을 하나 선택해서 시작
2) 선택한 정점과 인접하는 정점들 중의 최소 비용의 간선이 존재하는 정점 선택
3) 모든 정점이 선택될 때 까지 1,2, 과정을 반복

서로소인 2개의 집합(2 disjoint-sets - union.find 활용 가능) 유지
    - Tree Vertices(트리 정점들) - MST 만들기 위해 선택된 정점들
    - Nontree Vertices(비트리 정점들) - 선택되지 x 정점들

# 그래프는 디버깅하는 법이 중요!!

예제 입력 값
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
"""



V, E = map(int,input().split())

# 인접 행렬 방식
import heapq # 이거 복습은 하자, 우선 순위큐 만드는 것
def prim(start):
    heap = []
    # MST 에 포함되었는지 여부
    MST = [0] * V # visited 배열

    heapq.heappush(heap,(0,start)) #(w,start), 가중치와 정점 정보, w기준 정렬 됨
    # 누적합 변수 선언
    sum_weight = 0
    while heap:
        # 가장 적은 가중치 가진 정점 pop
        weight, v = heapq.heappop(heap)

        # 이미 방문한 노드라면 pass,,, cycle 방지
        if MST[v]:
            continue

        # 방문 체크
        MST[v] = 1

        # 누적합 처리
        sum_weight += weight

        for next in range(V):
            # 갈 수 없다면 or 이미 방문했다면 pass
            if graph[v][next] == 0 or MST[next]:
                continue

            heapq.heappush(heap,(graph[v][next],next))
    return sum_weight
graph = [[0]*V for _ in range(V)]

for _ in range(E):
    s, e, w = map(int,input().split())
    graph[s][e] = w
    graph[e][s] = w

result = prim(0)
print(f'최소 비용 = {result}')

