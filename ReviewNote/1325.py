# def dfs(start,now):
#     global mx
    
#     if not adj[now]:
#         return
#     can_cnt[start] += 1
#     for node in adj[now]:
#         if not visited[node]:
#             visited[node] = 1
#             dfs(start,node)
#     mx = max(mx,can_cnt[start])
    

# n, m = map(int,input().split())
# adj= [[] for _ in range(n+1)]
# can_cnt = [0]*(n+1)
# for _ in range(m):
#     s, e = map(int,input().split())
#     adj[e].append(s)
# mx = -1
# for i in range(1,n+1):
#     visited = [0]*(n+1)
#     visited[i] = 1
#     dfs(i,i)
# for i in range(1,n+1):
#     if can_cnt[i] == mx:
#         print(i,end=' ')


import sys;input=sys.stdin.readline

n, m = map(int,input().split())
adj= [[] for _ in range(n+1)]
can_cnt = [0]*(n+1)
for _ in range(m):
    s, e = map(int,input().split())
    adj[e].append(s)
mx = -1
stack = []
for i in range(1,n+1):
    visited = [0]*(n+1)
    stack.append(i)
    visited[i] = True

    while stack:
        now = stack.pop()
        can_cnt[i] += 1
        for node in adj[now]:
            if not visited[node]:
                stack.append(node)
                visited[node] = 1
    mx = max(mx,can_cnt[i])

for i in range(1,n+1):
    if can_cnt[i] == mx:
        print(i, end=' ')    


