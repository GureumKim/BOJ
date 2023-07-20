#######################################
#   동   1   2   3   4   5   6   7   8   9   10
# 서 ===========================================
#  ||
# 1||   1   2   3   4   5   6   7   8   9   10
#  ||        
#  ||
# 2||       1   3   6   10  15  21    
#  ||
#  ||
# 3||           1   4   10  20  35
# .||
# .||
# .||

# dp[N][M] = dp[N-1][M-1] + dp[N][M-1]

'''
DP(Dynamic Programming): 기본적인 아이디어로 
하나의 큰 문제를 여러 개의 작은 문제로 나누어서 
그 결과를 저장하여 다시 큰 문제를 해결할 때 사용하는 
것으로 특정한 알고리즘이 아닌 하나의 문제해결 패러다임

DP는 일반적인 재귀(Naive Recursion)방식과 유사한데
재귀는 시간 복잡도에 있어 비효율적일 수 있기에
DP를 사용하여 시간복잡도를 다항식 수준으로 줄인다.

DP 사용 조전

1) Overlapping Subproblems(겹치는 부분 문제)
2) Optimal Substructure(최적 부분 구조)

참조. https://hongjw1938.tistory.com/47
'''

# 풀이
import sys
input = sys.stdin.readline

T = int(input())

# dp[N][M] = dp[N-1][M-1] + dp[N][M-1]
arr = [[0 for _ in range(30)] for _ in range(30)]
for n in range(30):
    for m in range(30):
        if n == 0:
            arr[n][m]=m+1
        else:
            if n == m:
                arr[n][m] = 1
            elif n < m:
                arr[n][m] = arr[n-1][m-1] + arr[n][m-1]
                
for tc in range(T):
    N, M = map(int, input().rstrip().split()) #rstrip() 안해도 무관
    print(arr[N-1][M-1])


