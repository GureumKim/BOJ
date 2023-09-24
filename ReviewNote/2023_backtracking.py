def find_primes(num,level=1):
    # global cnt
    if level == n:
        # cnt += 1
        print(num)
        return
    for i in range(1,10):
        temp = num*10+i
        for j in range(2,int(temp**0.5)+1):
            if temp%j == 0:
                break
        else:
            find_primes(temp,level+1)

n = int(input())
# cnt = 0
find_primes(2)
find_primes(3)
find_primes(5)
find_primes(7)
# print(cnt)

# 	gunner6603 님 풀이
def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution():
    n = int(input())
    def dfs(curr):
        if curr is not None and len(str(curr)) == n:
            print(curr)
            return
            
        if curr is None:
            for i in range(2, 10):
                if is_prime(i):
                    dfs(i)
            return
                    
        for i in range(1, 10, 2):
            next_num = curr * 10 + i
            if is_prime(next_num):
                dfs(next_num)
    
    dfs(None)
    
solution()