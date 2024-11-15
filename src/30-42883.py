# https://school.programmers.co.kr/learn/courses/30/lessons/42883
# 탐욕법

def solution(number, k):
    stack = []
    
    for num in number:
        # top >= 오큰수일 때까지 pop
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    
    return "".join(stack[:len(number) - k]) # k가 남아있는 경우 고려
            
            