import sys; input = sys.stdin.readline
n = int(input())
# nums = sorted(map(int,input().split()))
nums = list(map(int,input().split()))
t = int(input())
nums.sort()
p1 = cnt = 0
p2 = n-1
while p2>p1:
    s = nums[p1] + nums[p2]
    if s == t:
        cnt += 1
        p1 += 1
        p2 -= 1
    elif s < t:
        p1 += 1
    else:
        p2 -= 1
print(cnt)