"""
feedback
: 조건에 따른 모든 상황(testcase)를 따져 보기
  익은 토마토가 적어도 한 개 들어있다는 말 없음, 이런 거 잘 체크하기
"""

from collections import deque
from sys import stdin; input = stdin.readline

def fill():
    global rest
    # 안익은 토마토만 있을 때 => unboundLocalError 해결 위해
    passed = 0

    while loc_ripe:
        y, x, passed = loc_ripe.popleft()
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            dy, dx = y + di, x + dj
            if 0 <= dy < n and 0 <= dx < m:
                if box[dy][dx] in (-1, 1): continue
                rest -= 1
                box[dy][dx] = 1
                loc_ripe.append((dy, dx, passed + 1))
    return passed

m, n = map(int, input().split())  # m x축 n y축
box = [list(map(int, input().split())) for _ in range(n)]

loc_ripe = deque()
rest = m * n
for i in range(n):
    for j in range(m):
        if box[i][j] == -1:
            rest -= 1
        elif box[i][j] == 1:
            loc_ripe.append((i, j, 0))
            rest -= 1
ans = fill()
print(ans) if not rest else print(-1)
