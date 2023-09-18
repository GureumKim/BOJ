# 분할 정복 위해 꼭 잘 풀어봐 mm이랑 같이 보기

# 민코딩 29.5 - 4

# 정렬
# 선택, 삽입, 버블 - n^2
# 계수(counting) - n
# 힙 합병 퀵 - nlogn

# 정렬은 면접의 단골 손님
# : 각 정렬 별 특징, 시간 복잡도



# 합병 정렬 메인 코드


# 합병 정렬
arr = [2,7,5,3,1,5,9,2]
result = [0]*8

def merge(start,end):
    global index,arr,index
    mid = (start+end)//2
    if start >= end: return

    # 쪼개기
    merge(start,mid)
    merge(mid+1,end)

    a = start
    b = mid + 1
    index = 0

    while 1:
        if a > mid and b > end: break
        if a > mid:
            result[index] = arr[b]
            index += 1
            b += 1
        elif b > end:
            result[index] = arr[a]
            index += 1
            a += 1
        elif arr[a]<=arr[b]:
            result[index] = arr[a]
            a += 1
            index += 1
        else:
            result[index]=arr[b]
            b += 1
            index += 1

    for i in range(index):
        arr[start+i] = result[i]


merge(0,7)
print(*result)


# 퀵 정렬
# 핵심 코드
# 4 1 7 9 6 3 3 6
arr = list(map(int,input().split()))
pivot = arr[0]

a = 1
b = len(arr) - 1

while 1:
    while a < len(arr) and arr[a]<=pivot:
        a += 1
    while b>=0 and arr[b]>pivot:
        b -= 1
    if a > b:
        break
    arr[a],arr[b] = arr[b],arr[a]
arr[0],arr[b] = arr[b],arr[0]
print(*arr)

# 완성하면

arr = [4,1,7,9,6,3,3,6]

def quick(start,end):
    if start >= end: return

    # 핵심 코드
    pivot=start
    a = start+1
    b=end

    while 1:
        while a <= end and arr[a] <= arr[pivot]:
            a+=1
        while b>= start and arr[b] > arr[pivot]:
            b-=1
        if a > b: break
        arr[a],arr[b] = arr[b],arr[a]
    arr[pivot],arr[b] = arr[b],arr[pivot]


    quick(start,b-1)
    quick(b+1,end)
quick(0,7)
print(*arr)

# 우선순위 큐
import heapq    # 이걸 쓴다
# from queue import priorityQueue # 이게 더 느리다

arr = [] # 함수 사용 시 이 리스트를 인자로 넘긴다!
# 루트 노드 이외의 정렬 크게 필요 x
heapq.heappush(arr,4)
heapq.heappush(arr,2)
heapq.heappush(arr,3)
heapq.heappush(arr,7)

# print(heapq.heappop(arr)) # 우선 순위 높은게 가장 먼저 출력
# print(heapq.heappop(arr))
# print(heapq.heappop(arr))
# print(heapq.heappop(arr))

for i in range(len(arr)):
    print(heapq.heappop(arr), end=' ')
print()

heapq.heappush(arr,4)
heapq.heappush(arr,2)
heapq.heappush(arr,3)
heapq.heappush(arr,7)
while arr:
    node = heapq.heappop(arr)
    print(node,end=' ')
# 시간 복잡도 logN

print()
# 오름차순으로 출력하기 (우선순위큐 사용)
import heapq
arr = [234,56,234,1,45,456,23]
heap = []
for i in range(len(arr)):
    heapq.heappush(heap,arr[i])
for i in range(len(arr)):
    print(heapq.heappop(heap),end=' ')

print()
# 방법 2
heapq.heapify(arr)  #heapify를 이용해서 한번에 heap의 자료형으로 바꾸기 가능
for i in range(len(arr)):
    print(heapq.heappop(arr),end=' ')
print()


# Max heap으로 바꾸기 1
import heapq
arr = [34,213,57,1,2,54,2,65]
heap = []
for i in range(len(arr)):
    heapq.heappush(heap,-arr[i]) # arr[i] 값에 음수를 줌(python)
for i in range(len(arr)):
    # print(heapq.heappop(heap)*-1)
    print(-heapq.heappop(heap))

# Max heap으로 바꾸기 1-1
import heapq
arr = [34,213,57,1,2,54,2,65]
heap = []
for i in range(len(arr)):
    heapq.heappush(heap,(-arr[i],arr[i]))
for i in range(len(arr)):
    print(heapq.heappop(heap)[1],end=' ')
print()
# Max heap으로 바꾸기 2

import heapq
arr = [34,213,57,1,2,54,2,65]
heap = []
heap = list(map(lambda x:-x,arr))
heapq.heapify(heap)
for i in range(len(arr)):
    print(-heapq.heappop(heap),end=' ')
print()

import heapq
n = int(input())
card = []
for i in range(n):
    heapq.heappush(card,int(input()))
ans = 0
while len(card)>1:
    temp1 = heapq.heappop(card)
    temp2 = heapq.heappop(card)
    ans+=(temp1,temp2)
    heapq.heappush(card,temp1+temp2)
print(ans)
