# 무조건 이 유형은 x, 그래도 자주나오는 방식
# DFS,BFS 먼저!!!

"""# 민코딩, 정올

코테 때 해쉬로 풀면 되는 경우 자주 있음
#DFS/BFS -> 해쉬(파이썬-딕셔너리, 가끔 counter모듈)[프로그래머스 문제]
-> 우선순위큐 -> 그리디, 다익스트라, 투포인터 -> Segment Tree, DP
"""

#

# longest common substring

def lcs(s1,s2):
    len1, len2 = len(s1),len(s2)
    arr = [[0]*(len2+1) for _ in range(len1+1)]

    Max = 0

    for i in range(1,len1+1):
        for j in range(1,len2+1):
            if s1[i-1] == s2[j-1]:
                arr[i][j] = arr[i-1][j-1]+1
                Max = max(Max,arr[i][j])
            else:
                arr[i][j] = 0
    return Max


s1,s2 = input(), input()
print(lcs(s1,s2))

# longest common subsequence
def lcs(s1,s2):
    len1,len2=len(s1),len(s2)
    arr=[[0]*(len2+1) for _ in range(len1+1)]

    for i in range(1,len1+1):
        for j in range(1,len2+1):
            if s1[i-1]==s2[j-1]:
                arr[i][j]=arr[i-1][j-1]+1
            else:
                arr[i][j]=max(arr[i-1][j],arr[i][j-1])
    return arr[len1][len2]

s1=input()
s2=input()
print(lcs(s1,s2))


# LIS
n = int(input()) # 정수의 개수
arr = list(map(int,input().split()))

result = [1]*n
for y in range(n):
    code = arr[y]   # 기준점
    for x in range(n):
        value = arr[x] # 비교대상
        if code > value:
            result[y]=max(result[x]+1,result[y])
print(max(result))