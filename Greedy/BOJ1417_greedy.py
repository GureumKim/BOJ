# 내 풀이
# 뒤에서 부터 max 찾아서 시간 줄여보려 했지만
# 그냥 편하게 library 쓰는게 이득이다
num = int(input())
dasom = int(input())
if num == 1:
    print(0)
else:
    others = []

    for idx in range(num-1):
        v = int(input())
        while idx>0 and others[idx-1] > v:
            idx -= 1
        others.insert(idx,v)
    masu = 0
    while dasom <= others[-1]:
        dasom +=1
        others[-1]-=1
        masu += 1
        for v in range(-1,-num+1,-1):
            if others[v] < others[v-1]:
                others[v],others[v-1] =  others[v-1],others[v]
            else:
                break
    print(masu)

# 다른 풀이
# import sys;input=sys.stdin.readline
n = int(input())
dasom, *others = [int(input()) for _ in range(n)]+[0] # 후보 한 명일 때 처리
                                        # 만약 n = 0 이면 dasom에 0 others는 none
masu = 0
while dasom <= max(others):
    mx = max(others) #위치 여기여야 다음에 mx 바뀜
    idx = others.index(mx) #첫 위치
    others[idx] -= 1
    dasom += 1
    masu += 1
print(masu)


