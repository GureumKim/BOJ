n,s,r = map(int,input().split())
broke = list(map(int,input().split()))
spare = list(map(int,input().split()))
data = [1]*(n+1)
for i in range(s):
    data[broke[i]] -= 1
# 겹치는 조건 확인!!
for i in range(r):
    data[spare[i]] += 1
    if spare[i] in broke:
        s -= 1
for i in range(1,n+1):
    if data[i] == 2:
        if data[i-1] == 0:
            s -= 1
        elif i< n and data[i+1]==0:
            data[i+1]=1
            s -= 1
print(s)