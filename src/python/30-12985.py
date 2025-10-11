# https://school.programmers.co.kr/learn/courses/30/lessons/12985
# 2017 팁스타운

from math import log

def solution(n,a,b):
    answer = 0
    
    if a > b: # a를 항상 작은 수로
        a, b = b, a
    
    for i in range(1, int(log(n, 2)) + 1):
        if (a + 1) // 2 == (b + 1) // 2:
            return i
        a = (a + 1) // 2
        b = (b + 1) // 2
        
    return int(log(n, 2))