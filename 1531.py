import sys; input = sys.stdin.readline
arr = [[0]*100 for _ in range(100)]
n, m = map(int,input().split())
cnt = 0

for _ in range(n):
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(y1-1,y2):
        for j in range(x1-1,x2):
            arr[i][j] += 1
            
for i in range(100):
    for j in range(100):
        if arr[i][j] > m:
            cnt += 1

print(cnt)