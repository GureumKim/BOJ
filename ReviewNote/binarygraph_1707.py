from sys import stdin, setrecursionlimit 
input = stdin.readline; setrecursionlimit(10**6)

def isbg(now,color=1):
    node[now] = color
   
    for next in adj[now]:
        if node[next]:
            if node[next] == color:
                return 0
        else:
            if not isbg(next,-color):   # 처음에 이거 전체를 리턴해서 실 => 다음 next를 알 수 가 없음!!
                return 0
    return 1    # not adj[now]인 경우!!!

for _ in range(int(input())):
    v, e = map(int,input().split())
    adj = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int,input().split())
        adj[a].append(b)
        adj[b].append(a)

    node = [0]*(v+1)
    for i in range(1,v+1):
        if not node[i]:
            ret = isbg(i)
            if not ret:
                break
    print("YES") if ret else print("NO")