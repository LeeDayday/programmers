# https://school.programmers.co.kr/learn/courses/30/lessons/42884
# 탐욕법

def solution(routes):
    answer = 0
    idx = 0
    routes.sort(key=lambda x: x[1]) # 나가는 시점 기준 오름차순 정렬
    
    while idx < len(routes):
        tmp_idx = idx + 1
        while tmp_idx < len(routes) and routes[idx][1] >= routes[tmp_idx][0]: # 현재 차량 진출 시점, 다음 차량 진입 시점 비교
            tmp_idx += 1
        answer += 1
        idx = tmp_idx
    
    return answer