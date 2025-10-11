# https://school.programmers.co.kr/learn/courses/30/lessons/68935
# 3진법 뒤집기

def dec_to_ter(n: int) -> list:
    result = []
    num = 0
    while True:
        q, r = n // 3, n % 3
        result.append(r)
        if q == 0:
            break
        n = n // 3
    return result

def ter_to_dec(data: list) -> int:
    result = 0
    num = 0
    for i in range(len(data) - 1, -1, -1):
        result += 3 ** num * int(data[i])
        num += 1
    return result

def solution(n):
    answer = dec_to_ter(n)
    answer = ter_to_dec(answer)
    
    return answer