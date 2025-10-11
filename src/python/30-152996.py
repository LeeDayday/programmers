# https://school.programmers.co.kr/learn/courses/30/lessons/152996
# 연습문제

from collections import Counter

def solution(weights):
    answer = 0
    data = Counter(weights)
    
    for weight, n in data.items():
        if n > 1: # 중복값끼리 계산
            answer += n * (n - 1) // 2 # nC2
            
        for x, y in [(2, 3), (2, 4), (3, 4)]:
            if weight * x / y in data: # 짝꿍 조건을 만족하는 경우
                answer += data[weight * x // y] * n

    return answer