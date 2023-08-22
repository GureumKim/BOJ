import sys; input = sys.stdin.readline
def cnt(arr,l=102):
    c = 0
    for lst in arr:
        for i in range(1,l):
            if lst[i-1] != lst[i]:
                c += 1
    return c

n = int(input())
arr = [[0]*102 for _ in range(102)]
for _ in range(n):
    x, y = map(int,input().split())
    for i in range(y,y+10):
        for j in range(x,x+10):
            arr[i][j] = 1
arr_t = list(zip(*arr)) # 전치 행렬, 수정하려면 list(map(list,zip(*arr))
print(cnt(arr)+cnt(arr_t))