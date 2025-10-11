# https://school.programmers.co.kr/learn/courses/30/lessons/131704
# 연습문제

def solution(order):
    answer = 0
    stack = [] # 보조 컨베이어 벨트
    
    for idx, num in enumerate(order):
        stack.append(idx+1) # 보조 컨베이어 벨트에 보관

        while stack and stack[-1] == order[answer]: # stack의 top과 배달 순서 비교
            stack.pop()
            answer +=1

    return answer