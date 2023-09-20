from sys import stdin; input = stdin.readline
n = int(input())
start_to_end = []
for _ in range(n):
    start_to_end.append(list(map(int,input().split())))
start_to_end = sorted(start_to_end,key=lambda x:(x[1],x[0]))

t_end = mcnt = 0
for i in range(n):
    if start_to_end[i][0] >= t_end:
        t_end = start_to_end[i][1]
        mcnt += 1

print(mcnt)