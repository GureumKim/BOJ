from collections import deque
from sys import stdin; input=stdin.readline


def check_power(y,x,team):
    global ans_w,ans_b
    # point : p를 누적해서 변경할 수 있는 변수로 설정해주어야 함!
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


## 지리는 풀이. jjujelly 님 풀이

n, m=map(int, input().split())
li=[]
li.append([0]*(n+2))
for i in range(m):
    a='0'
    a+=input()
    a+=('0')
    li.append(list(a))
li.append([0]*(n+2))
def dfs(x, y, a):
    if li[x][y]==a:
        li[x][y]=0
        return dfs(x+1, y, a)+dfs(x-1, y, a)+dfs(x, y+1, a)+dfs(x, y-1, a)+1
    return 0
W=0
B=0
for i in range(1, m+1):
    for j in range(1, n+1):
        if li[i][j]=='W':
            W+=dfs(i, j, 'W')**2
        elif li[i][j]=='B':
            B+=dfs(i, j, 'B')**2
print(W, B)