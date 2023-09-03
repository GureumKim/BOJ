import sys;input = sys.stdin.readline

def dfs(level = 0):
    if level == m:
        print(*temp)
        return
    
    # 전에 거랑 같은 거 나오면 back
    # 바로 뒤에 같은거 한 번 나오는 거는 오케이
    pre = 0
    for i in range(n):
        if chosen[i] or pre == nums[i]: continue
        chosen[i] = 1
        temp[level] = nums[i]
        pre = nums[i]
        dfs(level+1)
        chosen[i] = 0

n,m = map(int,input().split())
# 문자로 받으면 '100' vs '9'는 9가 더 뒤에 감 
nums = sorted(list(map(int,input().split())))
chosen = [0]*n
temp = [0]*m
dfs()