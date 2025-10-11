# https://school.programmers.co.kr/learn/courses/30/lessons/12924
# 연습문제

def solution(n):
    answer = 0
    start, end = 0, 0
    data = [i for i in range(1, n + 1)]
    
    while start <= end and end <= n:
        tmp = sum(data[start:end])
        if tmp < n:
            end += 1
            continue
        if sum(data[start:end]) == n:
            answer += 1
        start += 1
            
    return answer