# https://school.programmers.co.kr/learn/courses/30/lessons/42885
# 탐욕법

from collections import deque
def solution(people, limit):
    answer = 0
    # 보트 조건: 한 번에 최대 2명 / 최대 무게 제한: limit
    people.sort()
    people = deque(people)
    
    while people:
        # 무게 min + 무게 max 가 함께 탈 수 있는지 확인
        if len(people) > 1 and people[0] + people[-1] <= limit:
            people.pop()
            people.popleft()
        else: # 함께 탈 수 없는 경우, 무게 max 인원만
            people.pop()
        answer += 1
            
    return answer