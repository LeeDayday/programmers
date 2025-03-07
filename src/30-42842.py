# https://school.programmers.co.kr/learn/courses/30/lessons/42842
# 카펫

def solution(brown, yellow):
    total = brown + yellow
    
    # 약수 찾기 (반만 탐색하여 O(√N)으로 최적화)
    for num1 in range(1, int(total**0.5) + 1):
        if total % num1 == 0:
            num2 = total // num1  # num1과 num2는 약수쌍
            if (num1 - 2) * (num2 - 2) == yellow:
                return [max(num1, num2), min(num1, num2)]  # 가로 ≥ 세로 반환
