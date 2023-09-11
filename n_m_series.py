# n과 m -1
import sys;
input = sys.stdin.readline
def dfs(level=0):
    if level == m:
        print(*sequence)
        return
    for i in range(1, n + 1):
        if visited[i]: continue
        visited[i] = 1
        sequence[level] = i
        dfs(level + 1)
        visited[i] = 0


n, m = map(int, input().split())
sequence = [0] * m
visited = [0] * (n + 1)
dfs()

# n과 m -2
def dfs(start=1,level=0):
    if level == m:
        print(*choice)
        return
    for i in range(1,n+1):
        choice[level] = i
        dfs(i+1,level+1)

n, m = map(int,input().split())
choice = [0]*m
dfs()

# itertools 연습하기
# n과 m - 3
from itertools import product
n,m = map(int,input().split())
lst = [str(i) for i in range(1,n+1)]

print("\n".join(map(' '.join,product(lst,repeat=m))))

# 4
def dfs(start=1,level=0):
    if level == m:
        print(*choice)
        return
    for i in range(start,n+1):
        choice[level] = i
        dfs(i,level+1)

n, m = map(int,input().split())
choice = [0]*m
dfs()
# 4-2
from itertools import combinations_with_replacement as c_w_r
n, m = map(int,input().split())
lst = [str(i) for i in range(1,n+1)]
print("\n".join(map(' '.join,c_w_r(lst,m))))