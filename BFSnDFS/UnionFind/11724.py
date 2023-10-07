import sys; input = sys.stdin.readline

def find_root(x):
    if node[x] == 0:
        return x
    res = find_root(node[x])
    node[x] = res
    return res

def union(a,b):
    fa, fb = find_root(a), find_root(b)
    if fa == fb: return
    node[fb] = fa

n, m = map(int,input().split())
node = [0]*(n+1)
for _ in range(m):
    union(*map(int,input().split()))
# print(node[1:].count(0))
print(node.count(0)-1) # index 0의 0 카운트 취소