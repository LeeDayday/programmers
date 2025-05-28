# 복습 - 두 원 사이의 정수 쌍
# https://school.programmers.co.kr/learn/courses/30/lessons/181187

# O(N)

from math import sqrt, ceil
def solution(r1, r2):
    answer = 0
    # 1 사분면의 점 개수 구하고 전체에 적용하기
    for x in range(1, r2 + 1):
        max_y = int(sqrt(r2 ** 2 - x ** 2))
        if x < r1:
            min_y = ceil(sqrt(r1 ** 2 - x ** 2))
        else:
            min_y = 0
        # print(f"x={x} 일 때 y의 범위: [{min_y}, {max_y}]")
        answer += max_y - min_y + 1
    return answer * 4