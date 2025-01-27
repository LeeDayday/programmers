# https://school.programmers.co.kr/learn/courses/30/lessons/42746
# 연습문제

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : x * 3, reverse=True)
    
    return str(int(''.join(numbers)))