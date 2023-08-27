for t in range(1,11):
    n = int(input())
    field = [list(map(int,input().split())) for _ in range(n)]
    cnt = 0
    for j in range(n):
        stack = []
        for i in range(n): 
            if not stack and field[i][j] == 1:
                stack.append(1)
            elif stack and field[i][j] == 2:
                cnt += stack.pop() # 교착 상태 -> 1씩 더함
    print(f"#{t} {cnt}")