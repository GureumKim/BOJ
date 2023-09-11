# 11725
import sys; input=sys.stdin.readline
from collections import deque

def check():
    """
    부모가 있으면 continue
    아니면 부모 정보 입력
    루트노드(1번)에서 시작, queue(FIFO)를 활용하기 때문에
    자동으로 직전의 자식이 다음의 부모가 됨
    """
    for node in adj_lst[1]:
        q.append(node)
        p_data[node] = 1
        
    while q:
        parent = q.popleft()
        for sib in adj_lst[parent]:
            if p_data[sib]: continue
            p_data[sib] = parent
            q.append(sib) 

n = int(input())
adj_lst = [[] for _ in range(n+1)]

# p_data를 visited 배열로 활용
p_data = [0]*(n+1)
p_data[1] = 1

# 일단 부모, 자식 쪽 모두에 연결 정보 부여, p_data 배열을 통해 백트래킹
for _ in range(n-1):
    a, b = map(int,input().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)
q = deque()
check()
for i in range(2,n+1):
    print(p_data[i])