# https://school.programmers.co.kr/learn/courses/30/lessons/132265
# 연습문제

from collections import Counter

def solution(topping):
    answer = 0
    cake1 = Counter(topping)
    cake2 = set()
    for t in topping:
        cake1[t] -= 1
        if cake1[t] == 0:
            cake1.pop(t)
        cake2.add(t)

        if len(cake1) == len(cake2):
            answer += 1
    return answer