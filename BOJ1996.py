# 다른 사람들 코드보다 좀 느림, 개선 방안 필요
import sys;input=sys.stdin.readline
n = int(input())
field = [list(input().rstrip()) for _ in range(n)]

d_y = [-1,-1,-1,0,1,1,1,0]
d_x = [-1,0,1,1,1,0,-1,-1]
mine = []
m_l = 0
for i in range(n):
    for j in range(n):
        if field[i][j] == '.':
            field[i][j] = 0
        else:
            mine.append((i,j,int(field[i][j])))
            m_l += 1
            field[i][j] = '*'
for i in range(m_l):
    y, x, cnt = mine[i]
    for k in range(8):
        dy = d_y[k] + y
        dx = d_x[k] + x
        if dy<0 or dx<0 or dy>=n or dx >=n or field[dy][dx] in ['*','M']: continue
        field[dy][dx] += cnt
        if field[dy][dx] >= 10:
            field[dy][dx] = 'M'

for i in range(n):
    print(*field[i],sep='')


# 참고로 isdigit()은 str 자료형에서만 쓸 수 있음
# AttributeError: 'int' object has no attribute 'isdigit'