# 방법 1
# "10", 혹은 "01"의 패턴이 나타날 때마다 카운트하고
# cnt가 짝수일 경우 2로 나누고 홀수일 경우 2로나눈 몫에 +1해주면 된다.
import sys;input=sys.stdin.readline
num = list(input().rstrip())
cnt =0
for i in range(len(num)-1):
    if num[i] != num[i+1]:
        cnt +=1
if cnt % 2 == 0:
    print(cnt // 2)
else:
    print(cnt // 2 + 1)

# 방법 2
"""
python에서 
함수 명령어(?)를 변수로 저장해서
아래처럼도 호출이 가능하다
(c에서도 비슷한게 있언던 것 같다.)

"01"과 "10" 패턴의 갯수를 count함수를 통해 구하고
최대값을 출력한다.
"""
cnt=input().count
print(max(cnt("01"),cnt("10")))