# https://school.programmers.co.kr/learn/courses/30/lessons/138476
# 연습문제제

from collections import Counter

def solution(k, tangerine):
    answer = 0
    data = Counter(tangerine)

    for _, cnt in data.most_common():
        k -= cnt
        answer += 1
        if k <= 0:
            break
        
    return answer
