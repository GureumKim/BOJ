# 1번 풀이
import sys;input=sys.stdin.readline
def check(group,start=0,level = 0):
    global mn
    if level == 3:
        cnt = 0
        for i in range(2):
            for j in range(i+1,3):
                for idx in range(4):
                    if group[i][idx] != group[j][idx]:
                        cnt += 1 
        mn = min(mn,cnt)
        return
    for i in range(start,n):
        group[level] = mbti[i] 
        check(group,i+1,level+1)
for _ in range(int(input())):
    n = int(input())
    
    if n > 32:
        input()
        print(0)
        continue
    
    mbti = input().split()
    group = [0]*3
    mn = 21e8
    check(group)
    print(mn)

# 2번 풀이(better)
import sys;input=sys.stdin.readline
from itertools import combinations

def check(group):
    dist = 0
    for i in range(2):
        for j in range(i+1,3):
            for k in range(4):
                if group[i][k] != group[j][k]:
                    dist += 1
    return dist


for _ in range(int(input())):
    n = int(input())
    
    if n > 32:
        input()
        print(0)
        continue
    else:
        mn = 8 # 최소 거리의 범위: 2~8
        for group in combinations(input().split(),3):
            mn = min (mn,check(group))
            if mn == 2:
                break
        print(mn)