# BOJ2304

import sys;input = sys.stdin.readline
n = int(input())
height = [0]*1001
max_h = max_l =  0

for i in range(n):
    l, h = map(int,input().split())
    height[l] = h
    if h > max_h:
        max_h = h
        max_l = l
        
max_h = ans = 0
for i in range(max_l):
    max_h = max(max_h,height[i])
    ans += max_h

max_h = 0
for i in range(1000,max_l-1,-1):
    max_h = max(max_h,height[i])
    ans += max_h
print(ans)

    

        

 