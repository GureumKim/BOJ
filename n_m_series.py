# # # n과 m -1
# # import sys;
# #
# # input = sys.stdin.readline
# #
# #
# # def dfs(level=0):
# #     if level == m:
# #         print(*sequence)
# #         return
# #     for i in range(1, n + 1):
# #         if visited[i]: continue
# #         visited[i] = 1
# #         sequence[level] = i
# #         dfs(level + 1)
# #         visited[i] = 0
# #
# #
# # n, m = map(int, input().split())
# # sequence = [0] * m
# # visited = [0] * (n + 1)
# # dfs()
# #
# #
# # # n과 m -2
# # def dfs(start=1, level=0):
# #     if level == m:
# #         print(*choice)
# #         return
# #     for i in range(1, n + 1):
# #         choice[level] = i
# #         dfs(i + 1, level + 1)
# #
# #
# # n, m = map(int, input().split())
# # choice = [0] * m
# # dfs()
# #
# # # itertools 연습하기
# # # n과 m - 3
# # from itertools import product
# #
# # n, m = map(int, input().split())
# # lst = [str(i) for i in range(1, n + 1)]
# #
# # print("\n".join(map(' '.join, product(lst, repeat=m))))
# #
# #
# # # 4
# # def dfs(start=1, level=0):
# #     if level == m:
# #         print(*choice)
# #         return
# #     for i in range(start, n + 1):
# #         choice[level] = i
# #         dfs(i, level + 1)
# #
# #
# # n, m = map(int, input().split())
# # choice = [0] * m
# # dfs()
# # # 4-2
# # from itertools import combinations_with_replacement as c_w_r
# #
# # n, m = map(int, input().split())
# # lst = [str(i) for i in range(1, n + 1)]
# # print("\n".join(map(' '.join, c_w_r(lst, m))))
# #
# #
# # # 5
# # def dfs(level=0):
# #     if level == m:
# #         print(*choice)
# #         return
# #     for i in range(n):
# #         if used[i]: continue
# #         used[i] = 1
# #         choice[level] = lst[i]
# #         dfs(level + 1)
# #         used[i] = 0
# #
# #
# # n, m = map(int, input().split())
# # lst = list(map(int, input().split()))
# # lst.sort()
# # choice = [0] * m
# # used = [0] * n
# # dfs()
# #
# # # 5 -2
# # from itertools import permutations as pm
# #
# # n, m = map(int, input().split())
# # lst = list(input().split())
# # print('\n'.join(map(' '.join, pm(sorted(lst, key=lambda x: (len(x), x)), m))))
# #
# # # 6
# # from itertools import combinations as comb
# #
# # n, m = map(int, input().split())
# # lst = list(input().split())
# # print('\n'.join(map(' '.join, comb(sorted(lst, key=lambda x: (len(x), x)), m))))
# #
# # # 7
# # from itertools import product
# #
# # n, m = map(int, input().split())
# # lst = list(input().split())
# # print('\n'.join(map(' '.join, product(sorted(lst, key=lambda x: (len(x), x)), repeat=m))))
# #
# # # 8
# # from itertools import combinations_with_replacement as c_r
# #
# # n, m = map(int, input().split())
# # print('\n'.join(list(map(' '.join, c_r(sorted(list(input().split()), key=lambda x: (len(x), x)), m)))))
# # from itertools import combinations
# # n,m = map(int,input().split())
# # print('\n'.join(list(map(' '.join,combinations(sorted(list(input().split()),key=lambda x:(len(x),x)),m)))))
#
#
# # 10 - 매우 중요!!!!
# def dfs(start=0,level=0):
#     if level == m:
#         print(*choice)
#         return
#     pre = -1
#     for i in range(start,n):
#         if lst[i] == pre: continue
#         choice[level] = lst[i]
#         pre = lst[i]
#         dfs(i+1,level+1)
#
# n,m = map(int,input().split())
# lst = sorted(input().split(),key=lambda x:(len(x),x))
# choice = [0]*m
# dfs()
#
# # 위 방법에다 아니면 그냥 set 써서 해줄 수도 있다
#
def dfs(level=0):
    if level == m:
        print(*choice)
        return
    for i in range(len(lst)):
        choice[level] = lst[i]
        dfs(level+1)

n,m = map(int,input().split())
lst = sorted(set(input().split()),key=lambda x:(len(x),x))
choice = [0] *m
dfs()
#
#
