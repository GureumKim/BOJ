# dfs로는 별로인 문제
# 왜냐하면 가장 멀리까지 갈 수 있는 거리가 중요한데(최단 거리를 통해)
# 한 루트가 빙돌아가는 루트라면 도중에 visited배열에 이미 처리가 되어 있으므로
# 해당 위치에 도착한 시간을 기준으로 분기해야 함
# 참고 https://todaycode.tistory.com/110

def dfs(y,x,level=1):
    global ans


    dry, drx = [-1,1,0,0], [0,0,-1,1] # 상, 하, 좌, 우
    opp = [1,0,3,2] # 하,상,우,좌
    types = [[0,0,0,0],[1,1,1,1],[1,1,0,0],[0,0,1,1],[1,0,0,1],[0,1,0,1],[0,1,1,0],[1,0,1,0]]

    if level == l:
        return

    for k in range(4):
        dy,dx = y+dry[k], x+drx[k]
        if dy<0 or dy>=n  or dx<0 or dx>=m: continue
        if visited[dy][dx] ==0:
            if types[tunnel[y][x]][k] ==1 and types[tunnel[dy][dx]][opp[k]]==1:
                ans += 1
                visited[dy][dx] = visited[y][x]+1
                dfs(dy,dx,level+1)
        elif level+1<visited[dy][dx]:
            if types[tunnel[y][x]][k] ==1 and types[tunnel[dy][dx]][opp[k]]==1:
                visited[dy][dx] = level+1
                dfs(dy,dx,level+1)


for tc in range(1,int(input())+1):
    n,m,r,c,l = map(int,input().split())        # 세, 가
    tunnel = [list(map(int,input().split())) for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    visited[r][c] = 1
    
    ans = 1
    dfs(r,c)

    print(f"#{tc} {ans}")


# bfs로 하자
from collections import deque

t_types = [
    [0,0,0,0],
    [1,1,1,1],
    [1,1,0,0],
    [0,0,1,1],
    [1,0,0,1],
    [0,1,0,1],
    [0,1,1,0],
    [1,0,1,0]
]

di, dj = [-1,1,0,0],[0,0,-1,1]
opp = [1,0,3,2]

def bfs(si,sj):
    q = deque()
    visited = [[0]*m for _ in range(n)]
    ans = 0

    q.append((si,sj))
    visited[si][sj] = 1
    ans += 1

    while q:
        y,x = q.popleft()
        if visited[y][x] == l:
            return ans
        
        for i in range(4):
            ni,nj = y+di[i],x+dj[i]
            if 0<=ni<n and 0<=nj<m and visited[ni][nj]==0 \
            and t_types[tunnel[y][x]][i] == 1 and t_types[tunnel[ni][nj]][opp[i]]==1:
                q.append((ni,nj))
                visited[ni][nj] = visited[y][x] + 1
                ans += 1
    return ans

for tc in range(1,int(input())+1):
    n,m,r,c,l = map(int,input().split())
    tunnel = [list(map(int,input().split())) for _ in range(n)]
    
    ans = bfs(r,c)

    print(f"#{tc} {ans}")