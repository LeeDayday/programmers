# https://school.programmers.co.kr/learn/courses/30/lessons/12911
# 연습문제

def dec_to_bin(num):
    cnt = 0
    num = bin(num)
    for i in range(2, len(num)):
        if num[i] == '1':
            cnt += 1
    return cnt

def solution(n):
    answer = 0
    cnt = dec_to_bin(n)
    i = 1
    while True:
        if cnt == dec_to_bin(n + i):
            return n + i
        i += 1
        
    return answer