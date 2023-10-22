# 기타리스트 1495
# 참조
# https://resilient-923.tistory.com/272

n,s,m = map(int,input().split())
V = list(map(int,input().split()))

dp = [[0]*(m+1) for _ in range(n+1)]
dp[0][s] = 1

for i in range(n):
    for j in range(m+1):
        if dp[i][j] == 1:
            v1 = j + V[i]
            v2 = j - V[i]

            if v1<=m:
                dp[i+1][v1] = 1
            if 0<=v2<=m :
                dp[i+1][v2] = 1

ans = -1
for i in range(m+1):
    if dp[n][i]:
        ans = i
print(ans)