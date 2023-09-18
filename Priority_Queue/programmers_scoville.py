import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        temp = heapq.heappop(scoville)
        if not scoville:
            return -1
        answer += 1
        heapq.heappush(scoville,temp+2*heapq.heappop(scoville))
    return answer


