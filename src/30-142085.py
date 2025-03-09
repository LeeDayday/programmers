# https://school.programmers.co.kr/learn/courses/30/lessons/142085
# 연습문제

from heapq import heappush, heappop

def solution(n, k, enemy):
    e = len(enemy)
    if k >= e:
        return e
    
    answer = 0
    heap = []  # max heap (라운드 별 소모된 병사 저장. 기준: 병사 수)

    for i in range(e):        
        n -= enemy[i]
        heappush(heap, -enemy[i])  # 최대 힙에 추가
        if n < 0: # 병사가 부족하면 무적권 사용
            if k > 0:  
                n += -heappop(heap)  # 가장 큰 적을 무적권으로 처리
                k -= 1
            else:
                return i  # 병사도 없고 무적권도 없으면 종료
            
    return e
