'''
배열의 인덱스를 활용한 슬라이싱 문제이다.

느낀점
: 아직 이중 포문에서 인덱스를 활용한 문제 풀이가 익숙치 못하다.
특히 인덱스 범위 지정이 아직 많이 헷갈린다. 이런 문제를 많이 풀어야겠다. 
'''
# 방법 1, 리스트 append 이용
s = input()
l = len(s)-1

results=[]
for i in range(l-1):
    for j in range(i+1,l):
        result = s[i::-1]+s[j:i:-1]+s[-1:j:-1]
        results.append(result)
results.sort()
print(results[0])

# 방법 2 한 번에 다 해버리기
s = input()
l = len(s)-1

first = 'z'*50
for i in range(l-1):
    for j in range(i+1,l):
        result = s[i::-1]+s[j:i:-1]+s[-1:j:-1]
        if first > result:
            first = result
print(first)