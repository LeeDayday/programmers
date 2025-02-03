# https://school.programmers.co.kr/learn/courses/30/lessons/42839
# 소수 찾기

from itertools import permutations

def is_prime(num):
    if num < 2:
        return 0
    for i in range(2, num):
        if num % i == 0:
            return 0
    return 1

def solution(numbers):
    answer = 0
    data = set()
    for i in range(1, len(numbers) + 1):
        for perm in permutations(numbers, i):
            result = 0
            for num in perm:
                result *= 10
                result += int(num)
            data.add(result)
    for num in data:
        answer += is_prime(num)
    
    return answer