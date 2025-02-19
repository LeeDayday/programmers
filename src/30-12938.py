# https://school.programmers.co.kr/learn/courses/30/lessons/12938
# 연습문제

def solution(n, s):
    answer = []
    if n > s:
        return [-1]
    
    while n:
        mid = s // n
        answer.append(mid)
        n -= 1
        s -= mid
        
    answer.sort()
    return answer