from collections import deque
from sys import stdin; input = stdin.readline
def floodfill(q):
    global ripen_cnt, obstacle
    ans = 0
    while q:
        z,i,j,ans = q.popleft()
        for di, dj in [(1,0),(0,1),(-1,0),(0,-1)]:
            dy, dx = i + di, j + dj
            if dy<0 or dy>=n or dx<0 or dx>=m: continue
            if box[z][dy][dx] == 0:
                box[z][dy][dx] = 1
                ripen_cnt += 1
                q.append((z,dy,dx,ans+1))
        for dh in [-1,1]:
            dz = z+dh
            if dz<0 or dz>=h: continue
            if box[dz][i][j] == 0:
                box[dz][i][j] = 1
                ripen_cnt += 1
                q.append((dz,i,j,ans+1))
        
        # 인자 잘못 지정해준거 확인 용
        # for hh in range(h):
        #     for ii in range(n):
        #         print(*box[hh][ii])
        # print()

    if ripen_cnt+obstacle != m*n*h:
        ans = -1
    return ans

m,n,h = map(int,input().split())
box = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
q = deque()
# total 변수 선언 후 1,-1 일 때 하나 씩 빼줘도 되지만 보기 좋으라고 각 경우를 나눔
ripen_cnt, obstacle  = 0,0
for z in range(h):
    for i in range(n):
        for j in range(m):
            if box[z][i][j] == 1:
                q.append((z,i,j,0))
                ripen_cnt += 1
            elif box[z][i][j] == -1:
                obstacle += 1
print(floodfill(q))
