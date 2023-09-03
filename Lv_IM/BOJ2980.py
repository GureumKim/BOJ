import sys;input=sys.stdin.readline
n, l = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]
w = 0
for i in range(n):
    d, r, g = data[i]
    temp = (w+d)%(r+g)
    if temp < r:
        w += r - temp
print(l+w)


# 킹
import sys;input=sys.stdin.readline
comm = []
k,d,n = input().rstrip().split()
n = int(n)
for _ in range(n):
    comm.append(input().rstrip())
kx = ord(k[0])-64
ky = int(k[1])
dx =  ord(d[0])-64
dy =  int(d[1])

dir = {
    'R': (0,1),
    'L': (0,-1),
    'B': (-1,0),
    'T': (1,0),
    'RT': (1,1),
    'LT': (1,-1),
    'RB': (-1,1),
    'LB': (-1,-1)
}

for i in range(n):
    y = ky + dir.get(comm[i])[0]
    x = kx + dir.get(comm[i])[1]
    if y<1 or y>8 or x<1 or x>8:continue
    if y == dy and x == dx:
        yy = dy+dir.get(comm[i])[0]
        xx = dx+dir.get(comm[i])[1]
        if yy < 1 or yy >8 or xx <1 or xx>8:continue
        dy = yy; dx=xx
    ky=y; kx=x

print(chr(kx+64),ky,sep='')
print(chr(dx+64),dy,sep='')