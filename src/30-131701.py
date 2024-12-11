# https://school.programmers.co.kr/learn/courses/30/lessons/131701
# 연속 부분 수열 합의 개수

def solution(elements):
    answer = set()
    n = len(elements)
    elements = elements * 2
    for i in range(n):
        for j in range(1, n + 1):
            answer.add(sum(elements[i:i+j]))
    return len(answer)
