#https://sdev.tistory.com/521

n,m = map(int,input().split())
ans = [0]*26
for i in range(n):
    r = (i+1)*(2*n-i) + (i+n+1)*(n-i)
    now = input()
    for j in range(m):
        c = (j+1)*(2*m-j) + (j+m+1)*(m-j)
        ans[ord(now[j])-65] += r*c
print(*ans,sep='\n')