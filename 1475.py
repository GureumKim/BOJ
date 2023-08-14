import sys;input = sys.stdin.readline
nums = list(map(int,input().rstrip()))
cnts = [0]*10

for n in nums:
    cnts[n] += 1

if (cnts[6]+cnts[9])%2==0:
    cnts[6] = (cnts[6]+cnts[9])//2

else:
    cnts[6] = (cnts[6]+cnts[9])//2 + 1
cnts[9] = 0

print(max(cnts))