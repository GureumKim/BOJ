import sys; input = sys.stdin.readline

def cnt(arr):
    cnt = 0
    for lst in arr:
        for i in range(101):
            if lst[i-1] != lst[i]: cnt +=1
    return cnt 

n = int(input())
arr = [[0]*102 for _ in range(102)]
for _ in range(n):
    x, y = map(int,input().split())
    for i in range(y,y+10):
        for j in range(x,x+10):
            arr[i][j] = 1
arr_t = list(zip(*arr))
print(cnt(arr)+cnt(arr_t))
