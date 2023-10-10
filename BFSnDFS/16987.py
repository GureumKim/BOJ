"""
한 번도 안치는 경우 생각!!
+ 문제 잘 읽기 조건!!! 끝나는 level 값이 어디인지!!!

참고. https://www.acmicpc.net/board/view/39916
"""

n = int(input())
# eggs = [list(map(int,input().split())) for _ in range(n)]
# s,w = map(list,zip(*eggs))
# print(s,w)
s,w = [],[]
for _ in range(n):
    t_s, t_w = map(int,input().split())
    s.append(t_s)
    w.append(t_w)
# ss = deepcopy(s)
# s,w = map(list,zip(*eggs))

mx = 0
def dfs(now=0):
    global mx
    # print(s)
    if now == n:
        mx = max(mx,s.count(0))
        # print()
        return
    
    if s[now] == 0:
        dfs(now+1)
    else:
        flag = 0    # 한 번도 안 칠때를 flag를 통해 구현!!!
        for i in range(n):
            if s[i] and i != now:
                t_sn, t_si = s[now], s[i]
                s[now] -= w[i]
                s[i] -= w[now]
                if s[now] < 0:
                    s[now] = 0
                if s[i] < 0:
                    s[i] = 0
                dfs(now+1)
                s[now],s[i] = t_sn,t_si
                flag = 1
        if not flag:
            dfs(now+1)
             
        
dfs()
print(mx)

    
