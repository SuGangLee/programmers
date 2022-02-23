import heapq

def solution(scoville, K):
    #heapq.heapify(scoville) # 리스트를 힙 자료형으로 변환
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)
    answer = 0
    while heap[0] < K :  
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except IndexError:
            return -1
        answer+=1

    return answer

print(solution([1, 2, 3, 9, 10, 12],	7))