# https://school.programmers.co.kr/learn/courses/30/lessons/140107
# 연습문제

from math import sqrt

def solution(k, d):
    answer = 0
    for a in range(d // k + 1):
        limit = sqrt(d ** 2 - (a * k) ** 2)
        answer += int(limit) // k + 1

    return answer