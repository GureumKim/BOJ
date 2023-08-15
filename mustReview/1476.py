import sys;input = sys.stdin.readline
e, s, m = map(int,input().split())
y = 1
while 1:   
    if (y-e)%15 == 0 and (y-s)%28 == 0 and (y-m)%19 == 0:
        break
    else:
        y += 1
print(y)