from sys import stdin; input= stdin.readline

n , k = map(int,input().split())
# 구현을 쉽게 하기 위해 blank배열도 생성
knapsack = [[0]*(k+1) for _ in range(n+1)]

# w,v 정보를 갖는 item 배열 선언 및 아이템 추가
item = [[0,0]]
for _ in range(n):  
    item.append(list(map(int,input().split())))

for i in range(1,n+1):      # 아이템의 개수만큼
    for j in range(1,k+1):  # 최대 무게까지
        w,v = item[i][0], item[i][1]
        if j < w: # 가방에 넣을 수 없다면
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(knapsack[i-1][j],v+knapsack[i-1][j-w])
print(knapsack[n][k])   