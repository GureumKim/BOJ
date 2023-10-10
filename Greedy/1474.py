
## 실패 .. 
from sys import stdin; input = stdin.readline
n, m = map(int, input().split())
data = [input().rstrip() for _ in range(n)]
default_len, r = divmod(m - sum(map(len, data)), n - 1)
result = data[0]

for idx in range(1, n):
    if data[idx][0].islower() and r != 0:
        r -= 1
        result += '_' * (default_len + 1) + data[idx]
    elif idx + r == n:
        r -= 1
        result += '_' * (default_len + 1) + data[idx]
    else:
        result += '_' * default_len + data[idx]
print(result)




# n,m = map(int,input().split())
# words = dict()
# l = 0
# for _ in range(n):
#     a = input().rstrip()
#     l += len(a)
#     words[a] = a
# key = list(words.keys())
# # s_key = sorted(words.keys())

# div, mod = divmod(m-l,n-1)
# # print(div,mod)
# for i in range(1,n):
#     words[key[i]] = '_'*div +words[key[i]]

# for i in range(1,n):
#     if mod == 0: break
#     if key[i] > '_':
#         words[key[i]] = '_'+ words[key[i]]
#         mod -= 1
# if mod:
#     idx = n-1
#     while mod > 0:
#         if words[key[idx]][div] != '_':
#             words[key[idx]] = '_'+words[key[idx]]
#             mod -= 1
#         idx -= 1

# print(''.join(words.values()))

# # for i in range(1,n):
# #     words[key[i]] = '_'*div +words[key[i]]