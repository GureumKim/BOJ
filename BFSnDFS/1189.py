import sys;input=sys.stdin.readline

def dfs(y,x,dist=1):
    """
    way 배열에 이미 지났던 경우는 해당 자리에 값을 dist 값으로 바꿈(data 배열이 곧 visited 배열)
    추가로 백트래킹
    """
    global ans
    if dist > k:    # dist가 k를 초과할 경우 리턴
        return
    if y == 0 and x == c-1: # 목표 지점으로 도착했을 경우 dist와 k 값 비교 후 리턴
        if dist == k:
            ans += 1
        return
    for dy,dx in [(1,0),(0,1),(-1,0),(0,-1)]:   # 다이렉트 배열 활용한 탐색
        di = dy + y
        dj = dx + x
        if di >= r or dj >= c or di <0 or dj <0: continue
        if way[di][dj] == '.':
            way[di][dj] = dist
            dfs(di,dj,dist+1)
            way[di][dj] = '.'   # 다시 '.'으로 초기화

r,c,k = map(int,input().split())
way = [list(input().rstrip()) for _ in range(r)]
# 길에다 1 표시 했다가 다시 점 표시, 점일 때만 갈 수 있음
ans = 0
way[r-1][0] = 1
dfs(r-1,0) # 목표지점 : 0, c-1
print(ans)
