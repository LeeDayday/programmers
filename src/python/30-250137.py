# https://school.programmers.co.kr/learn/courses/30/lessons/250137
# PCCP 기출문제

def solution(bandage, health, attacks):
    curr_time = 0 # 현재 시간
    tmp_time = 0 # 연속 성공
    curr_health = health # 현재 체력
    
    for i in range(len(attacks)):
        a_time, a_damage = attacks[i]
        # 현재 시간 ~ 공격 수행 직전까지 붕대 감기 수행
        while curr_time + 1 < a_time :
            curr_time += 1
            if curr_time + 1 != a_time:
                tmp_time += 1
                curr_health += bandage[1]
            
            if tmp_time == bandage[0]: # 연속 회복 성공한 경우
                curr_health += bandage[2]
                tmp_time = 0

        curr_health = min(curr_health, health) # 최대 체력을 넘지 않도록
        # 공격 수행
        curr_health  -= a_damage
        tmp_time = 0
        # game over 여부 확인
        if curr_health <= 0:
            return -1
        
    return curr_health