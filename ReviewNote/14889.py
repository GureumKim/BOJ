import sys; input = sys.stdin.readline

def make_team(num=0,start=0):
    global mn
    if num == n//2:
        s1 = s2 = 0
        for i in range(n):
            for j in range(n):
                if team[i] and team[j]:
                    s1 += stat[i][j]
                elif not team[i] and not team[j]:
                    s2 += stat[i][j]
        mn = min(mn,abs(s1-s2))
        return
    for i in range(start,n):
        if not team[i]:
            team[i] = 1
            make_team(num+1,i+1)
            team[i] = 0

n = int(input())
stat = [list(map(int,input().split())) for _ in range(n)]
team = [0]*n
mn = float("inf")

make_team()
print(mn)