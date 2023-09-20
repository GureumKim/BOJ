# greedy
# 정렬 후 누적합

# n = int(input())
# p = sorted(map(int,input().split()))
# for i in range(1,n):
#     p[i] += p[i-1]
#
# print(sum(p))
#
# # 2번 풀이
# n = int(input())
# p = sorted(map(int,input().split()),reverse=1)
# ans = 0
# for i in range(1,n+1):
#     ans += (i*p[i-1])
# print(ans)



# 예제 https://www.acmicpc.net/problem/1931
# 끝나는 시간 기준 오름차순(sort)
# 하나 기입 => 다음 시작 시간은 앞의 끝나는 시간 보다 커야 함
n = int(input())
t_data = []
for _ in range(n):
    t_data.append(list(map(int,input().split())))

# 파티가 끝나느 시간 기준으로 sort
t_data = sorted(t_data,key=lambda x:(x[1],x[0]))
endtime = ans = 0
for i in range(n):
    if endtime<=t_data[i][0]:
        endtime = t_data[i][1]
        ans+=1
print(ans)