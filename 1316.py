N = int(input())
cnt = 0
for n in range(N):
    a = input()
    elms = list(set(a))

    start = 0
    end = 0
    flag = 1
    for e in elms:
        if flag == 0:
            break
        for idx in range(len(a)):
            if e == a[idx]:
                start = idx
                break
        for idx in range(len(a)-1,-1,-1):
            if e == a[idx]:
                end = idx
                break
        for i in range(start,end+1):
            if e != a[i]:
                flag = 0
                break
    if flag:
        cnt+=1
print(cnt)