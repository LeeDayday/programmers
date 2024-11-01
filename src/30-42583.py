# https://school.programmers.co.kr/learn/courses/30/lessons/42583
# 스택 / 큐

from collections import deque

def solution(bridge_length, weight, truck_weights):
    curr_weights = 0 # 현재 다리 위 트럭 무게
    total_time = 0 # 현재 시간
    truck_idx = 0 # 다음 진입할 트럭의 idx
    
    queue = deque()

    while True:
        # 다리를 건넌 트럭이 있는지
        if total_time > 0 and total_time == queue[0][1]:
            w, _ = queue.popleft()
            curr_weights -= w
            
        # 새로운 트럭이 들어갈 수 있는지
        if truck_idx < len(truck_weights):
            if curr_weights + truck_weights[truck_idx] <= weight:
                # 트럭 추가
                queue.append((truck_weights[truck_idx], total_time + bridge_length))
                curr_weights += truck_weights[truck_idx]
                truck_idx += 1
                
        total_time += 1
        if len(queue) == 0:
            break        
    return total_time

