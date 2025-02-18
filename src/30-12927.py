# https://school.programmers.co.kr/learn/courses/30/lessons/12927
# 연습문제제

from heapq import heappush, heappop
def solution(n, works):
    answer = 0
    maxheap = []
    for work in works:
        heappush(maxheap, -work)
        
    for _ in range(n):
        if not maxheap: # 더 이상 남은 작업이 없는 경우, 종료
            break
        max_work = heappop(maxheap)
        max_work += 1
        if max_work != 0:
            heappush(maxheap, max_work)
            
    if maxheap:
        for i in range(len(maxheap)):
            answer += maxheap[i] ** 2
        
    return answer