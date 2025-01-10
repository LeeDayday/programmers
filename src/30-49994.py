# https://school.programmers.co.kr/learn/courses/30/lessons/132265
# 연습문제

move = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
def solution(dirs):
    answer = 0
    visited = set() # (출발좌표, 도착좌표) 정보 저장
    curr_x, curr_y = 0, 0 # 현재 위치
    
    for cmd in dirs:
        
        new_x = curr_x + move[cmd][0]
        new_y = curr_y + move[cmd][1]

        # 범위 내에 존재
        if -5 <= new_x <= 5 and -5 <= new_y <= 5:
            # 새롭게 방문하는 경우
            if (curr_x, curr_y, new_x, new_y) not in visited: # 양방향 경로 고려
                # visited 추가 (양방향 추가)
                visited.add((curr_x, curr_y, new_x, new_y))
                visited.add((new_x, new_y, curr_x, curr_y))
                answer += 1
            # 현재 위치 갱신
            curr_x = new_x
            curr_y = new_y

        
    return answer