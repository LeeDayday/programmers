# https://school.programmers.co.kr/learn/courses/30/lessons/42627
# 힙(Heap)

from heapq import heappush, heappop


def solution(jobs):
    jobs.sort() # 시작 시간 기준 정렬
    heap = [] # 실행 가능한 작업을 소요 시간 기준 heap 정렬 (min heap)
    curr_time = 0 # 현재 시간
    total = 0 # 요청 ~ 종료 총 시간
    job_idx = 0
    
    while job_idx < len(jobs) or heap:
        # 현재 시간 기준 실행 가능한 job heappush
        while job_idx < len(jobs) and jobs[job_idx][0] <= curr_time:
            heappush(heap, (jobs[job_idx][1], jobs[job_idx][0]))
            job_idx += 1
        # 힙에 처리할 작업이 있는 경우
        if heap:
            exec_time, start_time = heappop(heap)
            curr_time += exec_time
            total += curr_time - start_time
        # 작업이 없는 경우
        else:
            # 다음 작업의 시작 시간으로 현재 시간 갱신
            curr_time = jobs[job_idx][0]
    return total // len(jobs)
            