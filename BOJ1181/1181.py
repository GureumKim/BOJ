"""
보완할 점: 이중 포문 외의 더 빠르고 간결한 방법이 있을까 생각해보기 
sol) -> (코드 리뷰 및 백준 풀이 탐구 후 내용 추가할 것)
"""
def swap(a,b):  
    """
    swap을 함수로 구현, 
    [주의할 점] 결과 값을 return해주지 않으면 함수 내의 a는 로컬 변수라 전역 변수는 바뀌지 않음
    """
    temp = a
    a = b
    b = temp
    return a ,b


N = int(input())
li = []
for i in range(N):
    li.append(input())


for i in range(N-1):
    for j in range(i+1, N):    # 버블 정렬 느낌
        if len(li[i]) > len(li[j]):
            li[i], li[j] = swap(li[i], li[j])
        elif len(li[i]) == len(li[j]):
            for e1, e2 in zip(li[i],li[j]): # 편리해서 zip() 썼는데, range(len(li[i]))범위의 인덱스를 가지고 각각 따지는 게 N이 커질 수록 효과적일 것
                if e1 > e2:
                    li[i], li[j] = swap(li[i], li[j])
                    break       # 그래도 break 문 써서 불필요한 문자열 탐색을 방지 
                elif e1 < e2:
                    break
    
for elm in li:
    print(elm)