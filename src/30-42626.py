# https://school.programmers.co.kr/learn/courses/30/lessons/42626
# 힙(Heap)

from heapq import heappush, heappop

def solution(scoville, K):
    answer = 0
    heap = []
    
    for i in range(len(scoville)):
        heappush(heap, scoville[i])

    while heap[0] < K:
        # 모든 음식을 섞어도 나오지 않는 경우
        if len(heap) < 2:
            answer = -1
            break
        tmp = heappop(heap) + heappop(heap) * 2
        heappush(heap, tmp)
        answer += 1
    return answer