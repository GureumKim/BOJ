# # 예제
# lst = [0,7,-3,-5,-4,-2,6,5,-9,-1,0]
# l = len(lst)
# # inf = -int(21e8)
# # dp = [inf]*l
# dp = [0]*l
# for i in range(1,l):
#     jp1 = dp[i-1]
#     jp2=dp[i-2] # 마지막이 0 이어서 가능
#     jp3=dp[i//2]
#     dp[i]=jp1+lst[i]
#     if dp[i] < jp2+lst[i]:
#         dp[i] = jp2+lst[i]
#     if i%2 == 0 and dp[i]<jp3+lst[i]:
#         dp[i]=jp3+lst[i]
# print(dp[-1])

# 12
#
#
# arr = [
#     [0,1,2,2],
#     [1,3,4,1],
#     [5,8,1,4],
#     [9,1,78,0]
# ]
# dp = [[0]*4 for _ in range(4)] #accumulated_sum
#
# def sett()



# kanpsack

# n, k = map(int,input().split())
# knapsack = [[0 for _ in range(k+1)] for _ in range(n+1)]
#
# item = [[0,0]]
# for i in range(1,n+1):  # item 입력
#     item.append(list(map(int,input().split())))
#
# for i in range(1,n+1):  # 아이템의 개수만큼 반복
#     for j in range(1,k+1): # 최대 무게까지 반복
#         w = item[i][0]
#         value = item[i][1]
#         if j < w: # 가방에 넣을 수 없다면
#             knapsack[i][j] = knapsack[i-1][j]
#         else: # 가방에 넣을 수 있다면
#             knapsack[i][j] = max(knapsack[i-1][j],value+knapsack[i-1][j-w])
#                 # 위에 값 vs 현재 아이템 가치 + 전 단계에서 구한 남은 무게 가치
# print(knapsack[n][k])


n,k = map(int,input().split())
coin = [0]
for i in range(n):
    don = int(input())
    coin.append(don)


arr = [[10001]*(k+1) for _ in range(n+1)]
arr[0][0] = 0
coin.sort()
for i in range(1,n+1):
    for j in range(1,k+1):
        mok = j//coin[i]
        if j%coin[i] == 0: arr[i][j] = mok
        else:
            if mok == 0:
                arr[i][j] = arr[i-1][j]
            else:
                arr[i][j]=min(arr[i-1][j],arr[i][j-coin[i]]+1)
if arr[n][k] >= 1001:
    print(-1)
else:
    print(arr[n][k])