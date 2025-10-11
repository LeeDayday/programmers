# https://school.programmers.co.kr/learn/courses/30/lessons/12973
# 2017 팁스타운운

def solution(s):
    stack = []
    
    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
        else:
            if stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])  
                
    if len(stack):
        return 0
    return 1
