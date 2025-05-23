# 복습 - 프로세스
# https://school.programmers.co.kr/learn/courses/30/lessons/42587

# O(NlogN)

from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque()
    
    for i in range(len(priorities)):
        queue.append((priorities[i], i)) # (우선순위, 프로세스 위치)
    
    priorities.sort(reverse=True)
    max_idx = 0
    while queue:
        # step 1    
        curr_priority, curr_idx = queue.popleft()

        # step 2
        if curr_priority < priorities[answer]:
            queue.append((curr_priority, curr_idx))
        # step 3
        else:
            answer += 1
            if curr_idx == location:
                break             
    return answer