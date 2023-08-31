# 2진수로 만들어 1의 개수 가지고 풀기

## 아이디어! cks537님(https://www.acmicpc.net/user/cks537) 풀이
import sys; input = sys.stdin.readline
n, k = map(int,input().split())
buy = 0
while bin(n).count('1') > k:
    expo = bin(n)[::-1].index('1')
    buy += 2**expo
    n += 2**expo
print(buy)


# 그냥 풀이
import sys; input = sys.stdin.readline
n, k = map(int,input().split())
buy = 0
while bin(n).count('1') > k:
    n += 1
    buy += 1
print(buy)