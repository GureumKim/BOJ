# 내가 푼 풀이 - 너무 느림(229,400 KB, 5632 ms, PyPy3 사용해야 통과)
import sys; input = sys.stdin.readline
Y = int(input())
cnt = 0
while Y >= 10:
    temp = list(map(int,str(Y)))
    Y = sum(temp)
    cnt += 1
print(cnt)
if not Y % 3: print('YES')
else: print('NO')


# 잘 푼사람(2753dudwns) 풀이 (https://www.acmicpc.net/source/53835824) 참고한 코드
Y = input().rstrip().replace("0","") #문자열로 받아서
cnt = 0
while len(Y)>1:
    Y = str(sum(Y.count(f"{i}")*i for i in range(1,10)))    #1-9의 수가 각각 몇개 있는지 활인 후 더해줌, 그 후 문자열로 형변환
    cnt += 1
print(f"{cnt}\nYES" if Y in "369" else f"{cnt}\nNO" )