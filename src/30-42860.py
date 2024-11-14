# https://school.programmers.co.kr/learn/courses/30/lessons/42860
# 탐욕법

def solution(name):
    answer = 0
    alphabet = [chr(ch) for ch in range(ord('a'), ord('z') + 1)]
    idx = 0
    
    # 상/하 조작
    def up_down(ch):
        return min(ord(ch) - ord('A'), ord('Z') - ord(ch) + 1)
    
    # 각 문자에 대해 상/하 조작 횟수 계산
    answer = sum(up_down(ch) for ch in name)
    
    # 좌/우 최소 이동 계산
    min_move = len(name) - 1  # 기본: 오른쪽으로 끝까지 가는 경우
    for i in range(len(name)): # i: 방향 전환 기준점
        next_idx = i + 1
        # 연속된 A 구간 찾기
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1
        # i까지 갔다가 뒤로 돌아가는 경우 계산
        min_move = min(min_move, 2 * i + len(name) - next_idx, i + 2 * (len(name) - next_idx))
    
    answer += min_move
    return answer

    