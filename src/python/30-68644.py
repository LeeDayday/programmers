# https://school.programmers.co.kr/learn/courses/30/lessons/68644
# 월간 코드 챌린지 시즌 1


from itertools import combinations


def solution(numbers):
    answer = set()
    for comb in combinations(numbers, 2):
        answer.add(sum(comb))
    answer = list(answer)
    answer.sort()
    return answer