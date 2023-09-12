# bfs로 패턴 구한 후 답을 찾았더니 메모리 초과로 실패했다.
# 메모리 초과도 신경을 써야 한다....
# 크기가 큰 배열(테스트 케이스 max 기준), 모듈 import 등... 최대한 줄인다
# -> 배열에 저장 없이 법칙 찾아서 구현한다.

# 맞은 코드

n, r1, c1, r2, c2 = map(int,input().split())
length = 2*n-1 
center_of_pattern = length//2
for i in range(r1,r2+1):
    x_dist = abs(center_of_pattern - i % length)
    for j in range(c1,c2+1):
        y_dist = abs(center_of_pattern - j % length)
        now = x_dist+y_dist
        if now >= n:
            print('.',end='')
        else:
            print(chr(now%26+97), end='')
    print()

# 틀렸던 코드(답은 나옴)
from collections import deque
def fill(sy,sx):
    q = deque()
    q.append((sy,sx,1))
    pattern[sy][sx] = 'a'
    while q:
        y,x,char = q.popleft()
        if char == n:
            break
        for k in range(4):
            dy = d_y[k]+y
            dx = d_x[k]+x
            
            if pattern[dy][dx] != '.': continue
            pattern[dy][dx] = chr(char%26 + 97)
            q.append((dy,dx,char+1))

n, r1, c1, r2, c2 = map(int,input().split())
l = 2*n-1
pattern = [['.']*(l) for _ in range(l)]

d_y = [1,0,-1,0]
d_x = [0,1,0,-1]
fill((l)//2,(l)//2)

for i in range(r1,r2+1):
    for j in range(c1,c2+1):
        print(pattern[i%(l)][j%(l)],end='')
    print()

# import 없이 구현해도 메모리 초과가 된다.
# 문제의 의도 자체가 배열에다가 패턴 저장하지 않고 바로
# 해당 좌표에 들어갈 값을 파악해 출력하는 것으로 이해된다.

# def fill(sy,sx):
#     q = []
#     q.append((sy,sx,1))
#     pattern[sy][sx] = 'a'
#     while q:
#         y,x,char = q.pop(0)
#         if char == n:
#             break
#         for k in range(4):
#             dy = d_y[k]+y
#             dx = d_x[k]+x
            
#             if pattern[dy][dx] != '.': continue
#             pattern[dy][dx] = chr(char%26 + 97)
#             q.append((dy,dx,char+1))