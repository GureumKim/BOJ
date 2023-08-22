import sys;input=sys.stdin.readline
n = int(input())
arr = [[0]*1001 for _ in range(1001)]

for k in range(1,n+1):
    x,y,w,h = map(int,input().split())
    for i in range(y,y+h):
        arr[i][x:x+w] = [k]*w # 2중 포문 대신 슬라이스로 가능
size = [0]*(n+1)

for i in range(1001):
    for j in range(1001):
        size[arr[i][j]] += 1
for i in range(1,n+1):
    print(size[i])