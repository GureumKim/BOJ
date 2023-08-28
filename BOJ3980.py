import sys;input =sys.stdin.readline
def dfs(level = 0):
    global mx
    if level == 11:
        mx = max(mx,sum(choice))
        return
    for i in range(11):
        if S[level][i] and not choice[i]:
            choice[i] = S[level][i]
            dfs(level+1)
            choice[i] = 0

tc = int(input())
for _ in range(tc):
    mx = -1
    used = [0] * 11
    choice = [0] * 11
    S = [list(map(int,input().split())) for _ in range(11)]
    dfs()
    print(mx)