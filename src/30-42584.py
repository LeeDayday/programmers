# https://school.programmers.co.kr/learn/courses/30/lessons/42584
# 스택/큐

def solution(prices):
    n = len(prices)
    answer = [0] * (n)
    stack = [] # 가격이 떨어지지 않은 prices의 index
    
    for i in range(n):
        # stack pop 여부 확인 (가격이 떨어졌는지 확인)
        while stack and prices[stack[-1]] > prices[i]:
            tmp = stack.pop()
            answer[tmp] = i - tmp
        stack.append(i)
    
    # 남은 stack 처리 (가격이 떨어진 적이 없는 index)
    while stack:
        tmp = stack.pop()
        answer[tmp] = n - 1 - tmp
    
    return answer