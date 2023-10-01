n,m = map(int,input().split())
count = 0

before = [list(map(int,input())) for _ in range(n)] 
after = [list(map(int,input())) for _ in range(n)]

# 변환
def convert(i,j):
    for r in range(i,i+3):
        for c in range(j,j+3):
            before[r][c] = 1 - before[r][c]

# n-2,m-2번 index까지 첫 점이 다르다면 변환
for i in range(n-2):
    for j in range(m-2):
        if before[i][j] != after[i][j]:
            convert(i,j)
            count += 1

# 변환 후 비교
for i in range(n):
    for j in range(m):
        if before[i][j] != after[i][j]:
            count = -1
            break

print(count)