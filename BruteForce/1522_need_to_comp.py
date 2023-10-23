# c 기준 1초 1억번
# 파이썬은 2000만번

## sort한 문자열 만들어서
# 시작 지점 하나씩 미뤄가면서 비교
word = list(input())
res = sorted(word)
mn = 21e8
cnt = 0
l = len(word)
for i in range(l):
    cnt = 0
    for j in range(l):
        if word[j] != res[(i+j)%l]:
            cnt +=1
    mn = min(cnt,mn)

# 교환이니까 한 위치가 다르다면 다른 위치도 다르게 된다. (문자열 수, a,b 각각의 개수 고정이니까)
print(mn//2)