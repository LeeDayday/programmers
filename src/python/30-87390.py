# https://school.programmers.co.kr/learn/courses/30/lessons/87390
# 월간 코드 챌린지 시즌3

def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        row = i // n
        col = i % n
        answer.append(max(row, col) + 1)
    return answer
