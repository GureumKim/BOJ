di = dict()
a = list(input())
for i in range(len(a)):
    if di.get(a[i],0):
        di[a[i]]+=1
    else:
        di[a[i]] = 1
b = list(input())
ans = len(a)
for i in range(len(b)):
    if di.get(b[i],0):
        di[b[i]]-=1
        ans -= 1
    else:
        ans += 1
print(ans)