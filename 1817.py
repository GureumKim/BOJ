import sys;input=sys.stdin.readline
n, m = map(int,input().split())
if n:       #상자에 들어갈 게 없을 때 처리
    weights = list(map(int,input().split()))
    cnt = 1
    s = 0
    for w in weights:
        if s + w <= m:
            s += w
        else:
            s = w
            cnt += 1
    print(cnt)
else:
    print(0)
# try & except 굳이 필요 없음..

