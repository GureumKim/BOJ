case = 1

while True:
    n = int(input())
    if n == 0:
        break
    girls = [input() for _ in range(n)]
    ring = [[] for _ in range(n)]
    for i in range(2*n-1):
        t1, t2 = input().split()
        ring[int(t1)-1].append(t2)
    for i in range(n):
        if len(ring[i]) < 2:
            print(f"{case} {girls[i]}")
    case += 1

