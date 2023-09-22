n, m = map(int,input().split())
inf = int(21e8)
adj = [[inf]*(n+1) for _ in range(n+1)]
for _ in range(m):
    s,e = map(int,input().split())
    adj[s][e] = 1
    adj[e][s] = 1
for ky in range(1,n+1):
    for si in range(1,n+1):
        for do in range(1,n+1):
            if adj[si][do] > adj[si][ky] + adj[ky][do]:
                adj[si][do] = adj[si][ky] + adj[ky][do]

mn = sum(adj[1])
min_idx = 1
for i in range(2,n+1):
    temp = sum(adj[i])

    if mn > temp:
        mn = temp; min_idx = i
print(min_idx)