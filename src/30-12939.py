# https://school.programmers.co.kr/learn/courses/30/lessons/12939
# 연습문제제
def solution(s):
    data = list(map(lambda x: int(x), s.split()))
    
    return str(min(data)) + " " + str(max(data))