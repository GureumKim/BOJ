# 16509
# 최소 => BFS
from collections import deque as dq
dir = {
    1:[(0,1),(1,1),(1,1)],
    2:[(1,0),(1,1),(1,1)],
    3: [(1,0),(1,-1),(1,-1)],
    4:[(0,-1),(1,-1),(1,-1)],
    5: [(0,-1),(-1,-1),(-1,-1)],
    6: [(-1,0),(-1,-1),(-1,-1)],
    7: [(-1,0),(-1,1),(-1,1)],
    8: [(0,1),(-1,1),(-1,1)]
}


def bfs(i,j):
    q = dq()
    q.append((i,j,0))

    while q:
        y,x,dist=q.popleft()
        for k in range(1,9):
            direct = dir.get(k)
            dy,dx = y,x
            for t in range(2):
                dy,dx = dy+direct[t][0], dx+direct[t][1]
                if dy>9 or dx>8 or dy<0 or dx<0: break
                if pan[dy][dx]==2: break # 일은 가상의 말(기억하기 위함)
            else:
                dy,dx = dy+direct[2][0],dx+direct[2][1]
                if dy >9 or dx >8 or dy < 0 or dx < 0 or pan[dy][dx]==1: continue # else는 반복문이 아니다!!
                # print(dy,dx)
                if pan[dy][dx] == 2:
                    return dist + 1
                pan[dy][dx] = 1
                q.append((dy, dx, dist + 1))
    return -1


pan = [[0]*9 for _ in range(10)] # 9행 8열
r1,c1 = map(int,input().split())
r2, c2 = map(int,input().split())
pan[r1][c1] = 1
pan[r2][c2] = 2

ans = bfs(r1,c1)

print(ans)