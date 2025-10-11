# https://school.programmers.co.kr/learn/courses/30/lessons/155651
# 연습문제

from heapq import heappush, heappop

# 10분을 추가한 문자열 결과 반환
def plus_ten_min(time):
    h, m = map(int, time.split(':'))
    m += 10
    if m >= 60:
        h += 1
        m -= 60
    return "{:02d}:{:02d}".format(h, m)

    
def solution(book_time):
    answer = 1 # 최초 방: ROOM 1
    book_time.sort()
    heap = []
    heappush(heap, plus_ten_min(book_time[0][1])) # (퇴실 시간 + 10분) 기준 최소힙
    
    for i in range(1, len(book_time)):
        # 기존 객실을 이어서 쓸 수 있는 경우
        if heap[0] <= book_time[i][0]:
            heappop(heap)
            
        heappush(heap, plus_ten_min(book_time[i][1]))
        answer = max(answer, len(heap))
    return answer