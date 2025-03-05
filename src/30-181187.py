# https://school.programmers.co.kr/learn/courses/30/lessons/181187
# 연습문제

from math import sqrt, ceil

def solution(r1, r2):
    answer = 0
    
    for x in range(1, r2 + 1):  # x를 1부터 r2까지 탐색 (대칭 활용)
        max_y = int(sqrt(r2**2 - x**2))  # r2 내부에서 가능한 y의 최대값
        min_y = ceil(sqrt(r1**2 - x**2)) if x < r1 else 0  # r1 내부를 제외하고 경계부터 시작

        answer += max_y - min_y + 1  
    
    return answer * 4  # 1사분면 기준으로 4배
