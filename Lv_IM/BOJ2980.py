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