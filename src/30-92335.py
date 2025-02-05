# https://school.programmers.co.kr/learn/courses/30/lessons/92335
# 2022 KAKAO BLIND RECRUITMENT

from math import sqrt

def dec_to_k(n, k):
    result = ''
    while n:
        result += str(n % k)
        n //= k
    return result[::-1]

def str_to_int(data):
    result = 0
    for d in data:
        result *= 10
        result += int(d)
    return result

def is_prime(num):
    num = str_to_int(num)
    if num <= 1:
        return 0
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return 0
    return 1
    
def solution(n, k):
    answer = 0
    result = dec_to_k(n, k)
    
    start, end = 0, 0
    while start < len(result):
        while end < len(result) and result[end] != '0':
            end += 1
        answer += is_prime(result[start:end])
        start = end
        end += 1
        
    return answer
