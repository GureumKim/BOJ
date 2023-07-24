"""
Sol) 
1.  속도 해결 
    - 문제 조건에서 문자열의 길이는 최대 50
    길이가 50인 이차 배열을 만들고 길이 별로 그룹화해서(클러스터링??) 입력을 받음
    그리고 각각의 그룹 내에서만 sort()메서드를 사용
2.  중복 제거
    - 입력 받을 때 해당 그룹에 입력 받을 값이 없어야
    입력 받게 함(not in 연산자 사용)

    set 타입을 사용하는 것도 생각 했지만
    형변환 많이 해야 되서 불편, 시간 걸려서 기각

3.  피드백
    - 속도: 1928 ms, 잘 푼 사람은 52ms ... 차이 너무 심함
    - 정렬 공부 아직 안했는데 다른 분들 풀이 보며 코드 구조 보완하기
    - 공부 후 코드 올리기
"""

import sys
input = sys.stdin.readline

categorize_len = [[] for i in range(50)]
N = int(input())
for _ in range(N):
    word = input().rstrip()
    if word not in categorize_len[len(word)-1]:
        categorize_len[len(word)-1].append(word)
for i in range(len(categorize_len)):
    categorize_len[i].sort()

for  words in categorize_len:
    for w in words:
        if w != '':
            print(w) 