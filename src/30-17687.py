# https://school.programmers.co.kr/learn/courses/30/lessons/17687
# [3차] n진수 게임

data = ['A', 'B', 'C', 'D', 'E', 'F']

def dec_to_n(target, n):
    result = ''
    while target:
        if target % n >= 10:
            result += data[target % n - 10]
        else:
            result += str(target % n)
        target = target // n
    return result[::-1]

def solution(n, t, m, p):              
    result = ['0']
    target = 1
    for _ in range(t * m):
        target_to_n = dec_to_n(target, n)
        for ch in target_to_n:
            result.append(ch)
        target += 1
    
    p -= 1
    answer = ''
    for _ in range(t):
        answer += result[p]
        p += m
    return answer