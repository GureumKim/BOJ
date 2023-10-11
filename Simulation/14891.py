from sys import stdin; input = stdin.readline

def spin(now,dir,check=0):
   
    if check == 0:
        next_l, next_r = now-1, now+1
        if now >0 and gears[next_l][2] != gears[now][6]:
            spin(next_l,dir*-1,-1)
        if next_r <4 and gears[next_r][6] != gears[now][2]:
            spin(next_r,dir*-1,1)
    elif check == 1:
        next_r = now+1
        if next_r < 4 and gears[next_r][6] != gears[now][2]:
            spin(next_r,dir*-1,1)
    else:
        next_l = now - 1
        if now >0 and gears[next_l][2] != gears[now][6]:
            spin(next_l,dir*-1,-1)
    if dir == -1:
        gears[now]= gears[now][1:]+[gears[now][0]]
    else:
        gears[now] = [gears[now][-1]] + gears[now][:7]

gears = [list(map(int,input().rstrip())) for _ in range(4)]
# print(gears)
k = int(input())
turns = [list(map(int,input().split())) for _ in range(k)]
# # print(turns)
for i in range(k):
    no, dir = turns[i]
    spin(no-1,dir)
    # print(gears)


ans = 0
for i in range(4):
    if gears[i][0]:
        ans += 1<<i # 1<<i이 점수
       
print(ans) 