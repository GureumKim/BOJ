import sys; input = sys.stdin.readline
from collections import deque

num = int(input())
adj_lst = [[] for _ in range(num+1)]
infected = [0]*(num+1)

q = deque()
ans = 0
for _ in range(int(input())):
    s, e = map(int,input().split())
    # 무방향 -> 양방향 처리 해줘야!!!!
    adj_lst[s].append(e)
    adj_lst[e].append(s)
infected[1] = 1
q.append(1)
while q:
    now = q.popleft()
    for com in adj_lst[now]:
        if infected[com]: continue 
        infected[com] = 1
        q.append(com)
        ans +=1
print(ans)
