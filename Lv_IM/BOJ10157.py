def fill(arr,r,c):
    direct = [(1,0),(0,1),(-1,0),(0,-1)]
    d = i = j = 0
    n = 1
    arr[i][j] = n
    n += 1
    while n <= r*c:
        i = direct[d][0] + i
        j = direct[d][1] + j
        if 0<=i<r and 0<=j<c and not arr[i][j]:
            arr[i][j] = n
            n += 1
        else:
            d = (d+1)%4
            continue  
        

def idx(n):
    if n > r * c: print(0); return
    for i in range(r):
        for j in range(c):
            if arr[i][j] == n:
                print(i,j);return
    
import sys;input=sys.stdin.readline
c, r = map(int,input().split())
k = int(input())
arr = [[0]*c for _ in range(r)]
fill(arr,r,c)
idx(k)
