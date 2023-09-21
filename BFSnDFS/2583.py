# 얘는 재귀 돌리면 recursion error 남 ==> 이때는 stack사용하면 된다

def dfs(i,j):
    global cnt
    stack = [(i,j)]

    while stack:
        i,j = stack.pop()

        for di,dj  in [(1,0),(0,1),(-1,0),(0,-1)]:
            dy, dx = i + di, j+dj
            if dy>=m or dx>=n or dy<0 or dx<0:continue
            if field[dy][dx] == 0:
                field[dy][dx] = 1
                cnt += 1
                stack.append((dy,dx))


m,n,k = map(int,input().split())    # y,j,k순
field = [[0]*n for _ in range(m)]

for i in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):
        field[i][x1:x2] = [1]*(x2-x1)

total = 0
ans = []
for i in range(m):
    for j in range(n):
        if field[i][j]: continue
        total += 1
        cnt = 1
        field[i][j] = 1
        dfs(i,j)
        ans.append(cnt)

print(total)
print(*sorted(ans))

"""
5 7 3
0 2 4 4
1 1 2 5
4 0 6 2
"""