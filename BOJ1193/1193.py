#분모  denominator
#분자   molecule

X = int(input())
n=1
sum1=1
# 등차수열의 합 공식 이용
# 1부터 n까지의 합이 X보다 커질 때까지 수행
# 대각으로 1개 -> 2개 -> 3개 -> ...
while sum1 < X:
    n+=1            
    sum1=int(n*(n+1)/2)     # n*(n+1)/2는 무조건 자연수이므로 int형변환 대신 //가 더 날 듯
i = sum1-X  # 초과한 정도


denom = 1   #분모
molecule =1 #분자
# n이 홀수, 짝수이냐에 따라
# 끝 값의 위치가 달라지므로 분기
# i만큼 넘어갔으니 넘어간 만큼 되돌아 가는 코드
if n % 2 ==1:   
    denom = n
    molecule = 1
    denom -= i
    molecule += i
else:
    denom = 1
    molecule = n
    denom += i
    molecule -= i
print(f"{molecule}/{denom}")