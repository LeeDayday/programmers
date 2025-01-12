# https://school.programmers.co.kr/learn/courses/30/lessons/17684
# 2018 KAKAO BLIND RECRUITMENT

from collections import defaultdict, deque

def solution(msg):
    data = defaultdict()
    for i in range(ord('A'), ord('Z') + 1):
        data[chr(i)] = i - ord('A') + 1
    answer = []
    msg = deque(msg)
    num = 27

    while msg:
        tmp = msg.popleft()
        while len(msg) and tmp + msg[0] in data:
            tmp += msg.popleft()
        if len(msg):
            data[tmp + msg[0]] = num
            num += 1
        answer.append(data[tmp])

    return answer

