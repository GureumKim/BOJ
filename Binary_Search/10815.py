import sys; input = sys.stdin.readline

def b_s(d,s,e):

    while s <= e:
        mid = (s + e) // 2
        if sang[mid] == d:
            return 1
        elif d > mid:
            s = mid + 1
        else:
            e = mid - 1
    return 0
#
#
#
n = int(input())
sang = sorted(map(int,input().split()))
m = int(input())
data = list(map(int,input().split()))


for i in range(m):
    print(b_s(data[i],0,n),end=' ')




