# https://school.programmers.co.kr/learn/courses/30/lessons/76502
# 월간 코드 챌린지 시즌2

from collections import deque 

def is_correct(s):
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}
    
    for i in range(len(s)):
        # 열린 괄호열은 stack에 push
        if s[i] in matching.values():
            stack.append(s[i])
        else:
            # 잘못된 괄호열: 빈 stack에 닫힌 괄호열을 push하려는 경우, 괄호열 쌍이 일치하지 않는 경우
            if not stack or matching[s[i]] != stack[-1]:
                return 0
            stack.pop()
            
    if stack:
        return 0
    return 1
            

def solution(s):
    answer = 0
    s = deque(s)
    for _ in range(len(s)):
        answer += is_correct(s)
        tmp = s.popleft()
        s.append(tmp)
    
    return answer