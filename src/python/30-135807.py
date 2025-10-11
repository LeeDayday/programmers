# https://school.programmers.co.kr/learn/courses/30/lessons/135807
# 연습문제

# 정수 a의 조건
# (영희 카드 % (철수 카드의 최대 공약수) != 0) 이나
# (철수 카드 % (영희 카드의 최대 공약수) != 0) 을 만족하는 정수의 최댓값
from math import gcd
from functools import reduce


def solution(arrayA, arrayB):
    answer = 0
    
    gcdA = reduce(gcd, arrayA) # 철수 카드의 최대 공약수
    gcdB = reduce(gcd, arrayB) # 영희 카드의 최대 공약수
    
    # gcdB가 arrayA의 모든 원소를 나누지 못해야 함
    if all(a % gcdB != 0 for a in arrayA):
        answer = max(answer, gcdB)

    # gcdA가 arrayB의 모든 원소를 나누지 못해야 함
    if all(b % gcdA != 0 for b in arrayB):
        answer = max(answer, gcdA)
    
    return answer