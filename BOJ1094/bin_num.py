import sys
input = sys.stdin.readline #이렇게 안해도 되지만 나중을 위해 미리 연습겸 사용했다.

# f-string 연습 겸, 문제 조건을 고려할 겸 7칸을 확보하여 공백을 0으로 표현했다.
num = f'{int(input().rstrip()):>07b}'
cnt = 0
for n in num:
    if n == '1':
        cnt += 1
print(cnt)