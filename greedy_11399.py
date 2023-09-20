# greedy
# 정렬 후 누적합

n = int(input())
p = sorted(map(int,input().split()))
for i in range(1,n):
    p[i] += p[i-1]

print(sum(p))