# 멱집합 ==> 강의 내용 구현하기
# 그림 그리고 구현해보기

# n-queen 문제 여러 번 풀기

def dfs(level=0):
    global ans
    if level == n:
        ans += 1
        return

    for j in range(n): # 열이니까 가독성 위해 j로, level이 행임
        if v1[j] == v2[level+j] == v3[level-j] == 0:
            v1[j] = v2[level+j] = v3[level-j] = 1
            dfs(level+1)
            v1[j] = v2[level + j] = v3[level - j] = 0

n = int(input())
ans = 0

v1 = [0]*n
v2 = [0]*(2*n-1) # i + j 끝 값 => n-1 + n-1 = 2n-2 거기에 1더함, + v2=v3=[0]*n하면 한꺼번에 움직인다
v3 = [0]*(2*n-1)
dfs()
print(ans)