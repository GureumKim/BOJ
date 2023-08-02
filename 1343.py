import sys;input = sys.stdin.readline    
a = list(input())
i = 0
cnt = 0
while i < len(a):
    if a[i] == 'X':
        cnt += 1
    if cnt == 4 :
        for j in range(i,i-4,-1):
            a[j] = 'A'
        cnt = 0
    if a[i] == '.' or a[i] == '\n':
        if cnt == 2:
            for j in range(i-1,i-3,-1):
                a[j] = 'B'
            cnt = 0
        elif cnt != 0:
            cnt = -1
            break
    i+=1
if cnt == -1:
    print(-1)
else:
    print("".join(a))