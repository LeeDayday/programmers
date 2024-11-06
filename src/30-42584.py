# https://school.programmers.co.kr/learn/courses/30/lessons/42584
# 스택/큐

from collections import deque
def solution(prices):
    answer = []
    tmp = deque(prices)
    for i in range(0, len(prices) - 1):
        tmp.popleft()
        cnt = 0
        for num in tmp:
            cnt += 1
            if prices[i] > num:
                break
        answer.append(cnt)
                
        
    answer.append(0)
    
    return answer