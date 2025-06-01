# https://school.programmers.co.kr/learn/courses/30/lessons/181188
# 연습문제

def solution(targets):
    answer = 0
    # 미사일 범위가 먼저 끝나는 순서대로 정렬
    targets.sort(key=lambda x: (x[1], x[0]))
    
    start, end = 0, 0 
    for target in targets:
        # 더 이상 요격 미사일을 공유할 수 없는 경우
        if target[0] >= end:
            end = target[1]
            answer += 1
    return answer