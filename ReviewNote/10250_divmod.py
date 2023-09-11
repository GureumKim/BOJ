# 몫과 나머지 계산할 때
# 나머지가 0이라는 거는 배수라는 거임
# 0 - n - 2n 이렇게
# 이를 아래에서 활용

# 구현 1
for _ in range(int(input())):
    h, w, n = map(int,input().split())
    a, b = divmod(n,h)
    if b == 0:
        print(f"{h}{a:02}")
    else:
        print(f"{b}{a+1:02}")

# 구현 2
for _ in range(int(input())):
    h, w, n = map(int,input().split())
    a, b = divmod(n,h)
    if b == 0:
        print(h*100+a)
    else:
        print(b*100+a+1)