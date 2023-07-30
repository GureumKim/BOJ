import sys
input=sys.stdin.readline
print = sys.stdout.write
Max = 1000000
S = [0] * (Max+1)
DP = [1] * (Max+1)
S[1] = 1
for i in range(2, Max+1):
    for j in range(1,(Max//i)+1):
        DP[i*j] += i
    S[i] = S[i-1]+DP[i]


T = int(input())
for tc in range(T):
    n = int(input())
    print(str(S[n])+"\n")


# 2
import sys
MAX = 1000000
dp = [0] * (MAX + 1)
s = [0] * (MAX + 1)
for i in range(1, MAX + 1): 
    j = 1 
    while i * j <= MAX: 
        dp[i * j] += i
        j += 1 
    s[i] = s[i - 1] + dp[i]
t = int(input()) 
for _ in range(t):
    a = int(sys.stdin.readline())
    sys.stdout.write(str(s[a])+"\n")
