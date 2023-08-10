# BruteForce 기법
# 일일이 전부,
# 시간 제한 2초, N은 10,000 보다 작거나 같은 수
# 최악의 경우 O(n), 문자열에 666있나 찾을 거니까
# O(m*n) ...? 시간 복잡도 계산 공부 필요

n = int(input())
num = 666
no = 0
while True:
    st = str(num)
    # 아래 처럼하면 너무 느리다.
    # for i in range(len(st)-2):
    #     for k in range(3):
    #         di = i+k
    #         if st[di] != '6':
    #             break
    #     else:
    #         no +=1
    # if no == n:
    #     break
# print(num)
    if '666' in st:
        no +=1
    if no == n:
        break
    num += 1
print(num)
