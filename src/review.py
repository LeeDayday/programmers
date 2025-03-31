# 복습 - 숫자 변환하기
# https://school.programmers.co.kr/learn/courses/30/lessons/152996

from collections import Counter

def solution(weights):
    answer = 0
    data = Counter(weights)

    for weight, cnt in data.items():
        if cnt > 1:
            answer += cnt * (cnt - 1) // 2 # nC2
        
        for a, b in [(2, 3), (2, 4), (3, 4)]:
            if weight * a / b in data:
                answer += data[weight * a // b] * cnt
    return answer

print(solution([100,180,360,100,270]))