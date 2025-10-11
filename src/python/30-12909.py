# https://school.programmers.co.kr/learn/courses/30/lessons/12909
# 스택 / 큐

def solution(s):
    answer = True
    
    stack = []
    
    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if len(stack) == 0:
                answer = False
                break
            stack.pop()
            
    if len(stack) > 0:
        answer = False
    return answer