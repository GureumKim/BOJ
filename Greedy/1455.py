# 거꾸로~
def shift(a,b):
    for i in range(0,a+1):
        for j in range(0,b+1):
            arr[i][j]= 1 if arr[i][j]==0 else 0 

n, m = map(int,input().split())
arr = [list(map(int,input())) for _ in range(n)]
cnt = 0
for j in range(m-1,-1,-1):
    for i in range(n-1,-1,-1):
        if arr[i][j]:
            shift(i,j)
            cnt += 1
print(cnt)

# **