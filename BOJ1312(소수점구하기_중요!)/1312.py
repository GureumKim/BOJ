
#1
import sys; input = sys.stdin.readline
A, B, N = map(int,input().split())


for _ in range(N):
    A = (A%B)*10
result = A//B
print(result)


#2 pow(a,b,[,z]) (a**b)%z (자리수에 관하여 자리 수 특정할 때 씀)
#아래와 같은 경우 n자리라면 10*b 모듈로 하면 n-1자리까지 나옴 이걸 
# 지수부분이랑 곱해서 b의 몫을 구하고 이것을 mod 10 하면 해당 자리 수의 값이 나오게 된다!
a, b, n = map(int, input().split())
print(a * pow(10, n, 10 * b) // b % 10)