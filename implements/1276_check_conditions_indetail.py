import sys;input=sys.stdin.readline
n = int(input())
lst = sorted([list(map(int,input().split())) for _ in range(n)],key=lambda x:x[0])
# print(lst)
covered = [0]*(10001)
ans = 2 * lst[0][0]
covered[lst[0][1]:lst[0][2]] = [lst[0][0] for _ in range((lst[0][2]-lst[0][1]))]
for i in range(1,n):
    ## 한 쪽만 조건에 해당한다!! 구현에 조건을 세세하게 따지기
    # 특히 문제에서 처럼 두 세개의 값 비교면 각각에 다른 조건이 적용될 수 있음을 인지하기
    for j in range(1,3):
        x = lst[i][j]
        if j == 2:
            x -= 1
        if covered[x]:
            ans += lst[i][0] - covered[x]
        else:
            ans += lst[i][0]
    covered[lst[i][1]:lst[i][2]] = [lst[i][0] for _ in range(lst[i][2]-lst[i][1])] #*(lst[i][2]-lst[i][1]+1)
print(ans)