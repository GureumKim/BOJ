# dfs
# import sys; input = sys.stdin.readline
# 입력 받음
n = int(input())
danji = [list(map(int,input())) for _ in range(n)]

def dfs(i,j):
    global cnt

    for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
        dy,dx = i + di, j+dj
        if dy >= n or dx >= n or dy<0 or dx<0: continue
        if danji[dy][dx]:
            cnt +=1
            danji[dy][dx] = 0
            dfs(dy,dx)

total = 0
ans = []
for i in range(n):
    for j in range(n):
        if danji[i][j]:
            cnt = 1
            total+=1
            danji[i][j]=0
            dfs(i,j)
            ans.append(cnt)
ans.sort()
print(total)
for i in range(total):
    print(ans[i])




# bfs
from collections import deque

n = int(input())
danji = [list(map(int,input())) for _ in range(n)]

def bfs(i,j):
    cnt = 1 # cnt 1부터 시작
    q = deque()
    q.append((i,j))

    while q:
        i,j = q.popleft()
        for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
            dy = di+i
            dx = dj+j
            if dy>=n or dx>=n or dy<0 or dx<0: continue
            if danji[dy][dx]:
                danji[dy][dx]=0
                cnt += 1
                q.append((dy,dx))
    return cnt

total = 0
ans = []
for i in range(n):
    for j in range(n):
        if danji[i][j]:
            total+=1
            danji[i][j]=0
            cnt = bfs(i,j)
            ans.append(cnt)
ans.sort()
print(total)
for i in range(total):
    print(ans[i])


