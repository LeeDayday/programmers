# https://school.programmers.co.kr/learn/courses/30/lessons/131704
# 연습문제

from collections import deque
def solution(order):
    answer = 0
    n = len(order)
    queue = deque() # 영재에게 전달되는 상자
    for num in range(1, n + 1):
        queue.append(num)
    stack = [] # 보조 컨베이어 벨트
    
    o_idx = 0
    # 보조 컨베이어 벨트 보관 후, order 와 비교하기
    while o_idx < n:
        # order와 일치하는 경우
        if stack and order[o_idx] == stack[-1]:
            stack.pop()
            answer += 1
            o_idx += 1
        else:
            # 일치하지 않는 경우, 보조 벨트에 보관
            if queue:
                stack.append(queue.popleft())
            # 더 이상 보관할 상자가 없는 경우, 종료
            else:
                break

    return answer