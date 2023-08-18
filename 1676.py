import sys;input = sys.stdin.readline
n = int(input())
facto = [0]*501
facto[0] = 1

for i in range(1,501):
    facto[i] = facto[i-1]*i
cnt = 0

while facto[n] % 10 == 0:
    facto[n] //= 10
    cnt += 1
print(cnt)