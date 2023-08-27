t = int(input())
for tc in range(1,t+1):
    n, m = map(int,input().split())
    flag = [list(input()) for _ in range(n)]
    maxx = -21e8
    for i in range(n-2):
        ans1 = 0
        for k in range(i+1):
            ans1 += flag[k].count('W')

        for k in range(i+1,n-1):
            ans2 = 0
            for j in range(i+1,k+1):
                ans2 += flag[j].count('B')
            for j in range(k+1,n):
                ans2 += flag[j].count('R')
            if ans1 + ans2 > maxx:
                maxx = ans1 + ans2
    print(f"#{tc}",n*m-maxx)
            

