# https://school.programmers.co.kr/learn/courses/30/lessons/42587
# 스택 / 큐

from collections import deque
def solution(priorities, location):
    answer = 0 # 실행 순서
    queue = deque()
    for i in range(len(priorities)):
        queue.append((priorities[i], i))
        
    priorities.sort(reverse=True)
    max_priority = priorities[answer]
    
    while queue:
        priority, process = queue.popleft()
        # 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있는 경우
        if priority < max_priority:
            # 다시 큐에 넣는다
            queue.append((priority, process))
        else:
            # 없는 경우, 프로세스 실행
            answer += 1
            if process == location:
                break
            # 최대 우선순위 갱신
            max_priority = priorities[answer]   
    
    return answer