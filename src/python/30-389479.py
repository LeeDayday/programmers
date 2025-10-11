# https://school.programmers.co.kr/learn/courses/30/lessons/389479
# 2025 프로그래머스 코드챌린지 2차 예선

from heapq import heappush, heappop
from math import ceil
def solution(players, m, k):
    answer = 0
    servers = [] # (서버 증설 시작 시간, 개수) minHeap으로 관리
    cnt = 0 # 실시간 증설된 서버의 수
    
    for i in range(len(players)):
        # 서버 반납
        while servers and servers[0][0] + k <= i:
            _, s = heappop(servers)
            cnt -= s
            
        # 증설된 서버가 수용가능한 인원
        available_player = (cnt + 1) * m - 1
        players[i] -= available_player
        
        # 추가적인 서버 증설이 필요한 경우
        if players[i] > 0:
            s = ceil(players[i] / m)
            cnt += s
            answer += s
            heappush(servers, (i, s))
            
    return answer