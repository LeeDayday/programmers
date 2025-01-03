# https://school.programmers.co.kr/learn/courses/30/lessons/76502
# 월간 코드 챌린지 시즌2

def rotate_s(s):
    return s[1:] + s[0] 

def is_correct(s):
    stack = []
    for i in range(len(s)):
        # 열린 괄호열은 stack에 push
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            stack.append(s[i])
        else:
            # stack이 빈 상태에서 닫힌 괄호열을 push하려는 경우: 잘못된 괄호열
            if len(stack) == 0:
                return 0
            top = stack.pop()
            # top과 s[i]가 일치하는 괄호쌍인지 확인
            if (top == '(' and s[i] == ')') or (top == '[' and s[i] == ']') or (top == '{' and s[i] == '}'):
                continue
            else:
                return 0
        
    if len(stack) > 0:
        return 0
    return 1
            

def solution(s):
    answer = 0
    rotated_s = s
    for _ in range(len(s)):
        answer += is_correct(rotated_s)
        rotated_s = rotate_s(rotated_s)
    
    return answer