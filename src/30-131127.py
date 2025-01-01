# https://school.programmers.co.kr/learn/courses/30/lessons/138476
# 연습문제

from collections import Counter

def solution(want, number, discount):
    answer = 0
    data = dict()
    for i in range(len(want)):
        data[want[i]] = number[i]

    for i in range(len(discount) - 9):
        if data == Counter(discount[i:i+10]):
            answer += 1

    return answer