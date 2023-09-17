from collections import deque
from sys import stdin; input=stdin.readline


def check_power(y,x,team):
    global ans_w,ans_b
    p = 1
    t = 1 if team == 'W' else 2
    q.append((y,x))
    st[y][x] = t
    while q:
        y,x = q.popleft()
        for ki, kj in [(1,0),(0,1),(-1,0),(0,-1)]:
            dy = y + ki
            dx = x + kj
            if dy <0 or dx <0 or dy >=m or dx >=n:continue
            if st[dy][dx] == team:
                st[dy][dx] = t
                p+=1
                q.append((dy,dx))
    if team == 'W':
        ans_w += p**2
    else:
        ans_b += p**2
        

n, m = map(int,input().split())
st = [list(input().rstrip()) for _ in range(m)]
print(st)
q = deque()
ans_w = ans_b = 0
for i in range(m):
    for j in range(n):
        if st[i][j] in ('W','B'):
            check_power(i,j,st[i][j])
print(ans_w, ans_b)