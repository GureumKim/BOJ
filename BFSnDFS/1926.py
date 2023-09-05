import sys;input = sys.stdin.readline
from collections import deque

def check_size(y,x,size=1):
    global mx
    q.append((y,x))
    fainted[y][x] = 1

    while q:
        y,x = q.popleft()
        for k in range(4):
            dy = d_y[k] + y
            dx = d_x[k] + x
            if dy<0 or dx<0 or dy>=n or dx>=m: continue
            if not canvas[dy][dx] or fainted[dy][dx]:continue
            fainted[dy][dx] = 1
            size += 1
            q.append((dy,dx))
    mx = max(mx,size)


d_y = [1,-1,0,0]
d_x = [0,0,1,-1]
n,m = map(int,input().split())
canvas = [list(map(int,input().split())) for _ in range(n)]
fainted = [[0]*m for _ in range(n)]

mx = 0  # 단, !! 조심하기!!, 조건 확실하게
num = 0
q = deque()
for i in range(n):
    for j in range(m):
        if canvas[i][j] and not fainted[i][j]:
            num += 1
            check_size(i,j)
print(num,"\n",mx,sep='')

