## 1st try - failed(RuntimeError)
# feeback: 테스트 케이스와 시간 복잡도를 먼저 고려하기

import sys;input=sys.stdin.readline

def dice_max(level,start):
    global total

    if level == n:
        return
    m = -1
    for i in range(6):
        if dices[level][i] == start:
            s = i
            index = link.get(s)
            break

    for i in range(6):
        if i == start or i == index:
            continue
        if dices[level][i] > m:
            m = dices[level][i]
    total += m
    dice_max(level+1,dices[level][index])

n = int(input())
dices = [list(map(int,input().split())) for _ in range(n)]
link = {
    0 : 5,
    1 : 3,
    2 : 4,
    3 : 1,
    4: 2,
    5: 0
}
maxx = 0

for i in range(6):
    total = 0
    m = -1
    idx = link.get(i)
    for d in range(6):
        if d == i or d == idx: continue
        if dices[0][d] > m:
            m = dices[0][d]
    total += m
    dice_max(1,dices[0][idx])
    if maxx < total:
        maxx = total
print(maxx)



# 2nd try - successed
# feedback: 딕셔너리에 아예 함수까지 넣어 버려 처리하면(각각에서 처리 할 수 있게)
# 더 빨라질 것 --> 잘 푼 사람들 풀이 보고 보완해보기

import sys; input=sys.stdin.readline
n = int(input())
dices = [list(map(int,input().split())) for _ in range(n)]
link = {
    0 : 5,
    1 : 3,
    2 : 4,
    3 : 1,
    4: 2,
    5: 0
}
maxx = 0

for i in range(6):
    total = 0
    m = -1
    idx = link.get(i)
    for d in range(6):
        if d == i or d == idx: continue
        if dices[0][d] > m:
            m = dices[0][d]
    total += m
    level = 1
    start  = dices[0][idx]
    while level < n:
        m = -1
        for i in range(6):
            if dices[level][i] == start:
                s = i
                idx = link.get(s)
                start = dices[level][idx]
                break
        for i in range(6):
            if i == s or i == idx: continue
            if dices[level][i] > m:
                m = dices[level][i]
        total += m
        level += 1

    if maxx < total:
        maxx = total

print(maxx)