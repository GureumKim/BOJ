# 만약 r,g,b아니고 가짓수 되게 여러가지면 ..? DP는 좋은 방법인가...? 탐구 필요
n = int(input())

dp = [[0]*3 for _ in range(n)]
cost = [list(map(int,input().split())) for _ in range(n)]
dp[0][0], dp[0][1],dp[0][2] = cost[0][0],cost[0][1],cost[0][2]

for i in range(1,n):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2])+cost[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2])+cost[i][1]
    dp[i][2] = min(dp[i-1][0],dp[i-1][1])+cost[i][2]
print(min(dp[n-1]))