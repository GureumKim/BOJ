# 절대거리 상대거리!

#1 절대거리 이용(추천)

import sys; input = sys.stdin.readline
def get_d(x, y):
    if x == 1:
        return y
    elif x == 2:
        return 2*w+h-y
    elif x == 3:
        return 2*(w+h) - y
    if x == 4:
        return w + y

w, h = map(int, input().split())
n = int(input())
dist = []
answer = 0

for _ in range(n + 1):
    x, y = map(int, input().split())
    dist.append(get_d(x, y))
for i in range(n):
    s1 = abs(dist[-1] - dist[i])
    s2 = 2 * (w + h) - s1
    answer += min(s1, s2)
print(answer)

#2 상대거리 이용

import sys; input = sys.stdin.readline
w, h = map(int, input().split())
n = int(input())
li = []
Sum = 0
for _ in range(n + 1):
    a, b = map(int, input().split())
    loc = {
        1: (0, b),
        2: (h, b),
        3: (b, 0),
        4: (b, w)
    }
    li.append((a, loc.get(a)))

l, dir = li.pop()

for i in range(n):
    if l == 1 and li[i][0] == 2 or l == 2 and li[i][0] == 1:
        Sum += min(dir[1] + li[i][1][1], 2 * w - (dir[1] + li[i][1][1]))
        Sum += h
    elif l == 3 and li[i][0] == 4 or l == 4 and li[i][0] == 3:
        Sum += min(dir[0] + li[i][1][0], 2 * h - (dir[0] + li[i][1][0]))
        Sum += w
    else:
        Sum += abs(dir[0] - li[i][1][0]) + abs(dir[1] - li[i][1][1])
print(Sum)