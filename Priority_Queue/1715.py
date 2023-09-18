from sys import stdin; input=stdin.readline
import heapq
ans = 0
heap = []
for _ in range(int(input())):
    heapq.heappush(heap,int(input()))

while 1:
    temp = heapq.heappop(heap)
    if not heap:
        break
    temp += heapq.heappop(heap)
    ans += temp
    heapq.heappush(heap, temp)
print(ans)