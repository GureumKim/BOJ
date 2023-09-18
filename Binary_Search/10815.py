import sys; input = sys.stdin.readline

# 방법 1
n = int(input())
di = dict()
for i in map(int,input().split()):
    di[i] = 1
m = int(input())
data = list(map(int,input().split()))

for i in data:
    print(di.get(i,0),end=' ')


# 방법2

import sys; input = sys.stdin.readline

def b_s(d,s,e):
    while s <= e:
        mid = (s + e) // 2
        if sang[mid] == d:
            return 1
        elif d > sang[mid]:
            s = mid + 1
        else:
            e = mid - 1
    return 0

n = int(input())
sang = sorted(map(int,input().split()))
m = int(input())
data = list(map(int,input().split()))

for i in range(m):
    print(b_s(data[i],0,n-1),end=' ')

# for i in range(m):
#     print(b_s(data[i],0,n-1),end=' ') # n이면 틀리고 n-1해야 됨 왜냐면 마지막 index가 n-1임


