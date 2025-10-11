# https://school.programmers.co.kr/learn/courses/30/lessons/42885
# 탐욕법

def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0 # 몸무게 min idx
    b = len(people) - 1 # 몸무게 max idx
    while a < b :
        if people[b] + people[a] <= limit : # 두 사람이 탈 수 있는 경우
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer # 전체 인원(모두 혼자 탄 경우) - 두 사람이 탄 경우