# 복습 - 호텔 대실
# https://school.programmers.co.kr/learn/courses/30/lessons/155651

# O(NlogN)
from heapq import heappush, heappop
def plus_ten_min(time):
    h, m = map(int, time.split(":"))
    m += 10
    if m >= 60:
        h += 1
        m -= 60
    return '{:02d}:{:02d}'.format(h, m)
    
def solution(book_time):
    answer = 1
    book_time.sort()
    heap = [] # (체크 아웃 + 10분) 기준 힙 정렬
    
    for i in range(len(book_time)):
        # 퇴실
        while heap and heap[0] <= book_time[i][0]:
            heappop(heap)
        # 체크인
        heappush(heap, plus_ten_min(book_time[i][1]))
        answer = max(answer, len(heap))
        

    return answer