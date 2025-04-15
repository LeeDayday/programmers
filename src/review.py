# 복습 - 올바른 괄호
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

# O(N)

def solution(s):
    if len(s) % 2:
        return False
    cnt = 0
    idx = 0
    while idx < len(s):
        if s[idx] == ')':
            cnt -= 1
            if cnt < 0:
                return False
        else:
            cnt += 1
        idx += 1
    if cnt > 0:
        return False
            
    return True