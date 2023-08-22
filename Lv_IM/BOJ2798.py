import sys; input = sys.stdin.readline
def comb(level=0,start=0,s = 0):
    global minn, ans
    if s > m:
        return
    if level == 3:
        if m-s < minn:
            minn = m-s
            ans = s
        return
    for i in range(start,n):
        comb(level+1,i+1,s+cards[i])

n,m = map(int,input().split())
cards = list(map(int,input().split()))
minn = 21e8
ans = 0
comb()
print(ans)
