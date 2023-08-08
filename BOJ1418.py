n = int(input())
k = int(input())

# 에라토스테네스의 체
lst_prime = [1]*(n+1)
for i in range(2,int(n**0.5)+1):
    if lst_prime[i]:
        for j in range(2*i,n+1,i):
            lst_prime[j] = 0
# n 이하 k 이상인 소수 제거
k_nums = [1]*(n+1)
for i in range(2,n+1):
    if lst_prime[i] and i > k:
        for j in range(i, n+1, i):
            k_nums[j] = 0
Sum = 0
for i in range(n+1):
    if k_nums[i] == 1:
        Sum += 1
print(Sum-1) # index ==0 일 때 값(1)을 빼줌 