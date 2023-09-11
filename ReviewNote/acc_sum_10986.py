import sys; input=sys.stdin.readline

n, m = map(int,input().split())
nums = list(map(int,input().split()))
asum = [nums[0]]+[0]*(n-1)
remainders = [0]*m
ans = 0

for i in range(1,n):
    asum[i] = nums[i]+asum[i-1]
for i in range(n):    
    remainder = asum[i]%m
    if remainder == 0:
        ans += 1
    remainders[remainder]+=1
for i in range(m):
    ans += remainders[i]*(remainders[i]-1)//2
print(ans)

# 딕셔너리로도 가능
# 빈 딕셔너리 생성
# 애초에 s = 0에다가 누적 합 받은 다음
# %m 해주고
# 그 나머지 값이 딕셔너리 키에 있음 +=1 없음 해당 나머지 값인 키를 생성 후 value를 1로 지정
# 그 후는 똑같음 value 값들을 조회해서 -> 적용 (n C 2 , n이 한 키의 value 값) 