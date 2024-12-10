# https://school.programmers.co.kr/learn/courses/30/lessons/42842
# 카펫

def solution(brown, yellow):
    area = brown + yellow

    for n in range(1, area // 2 + 1): # n: 세로
        if area % n == 0:
            m = area // n # m: 가로
            if (m - 2) * (n - 2) == yellow:
                return [m, n]
    return