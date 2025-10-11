# https://school.programmers.co.kr/learn/courses/30/lessons/388353
# 2025 프로그래머스 코드챌린지 1차 예선

dx = [0, 0, 1, -1]
dy = [1, -1, 0 ,0]

from collections import deque

def solution(storage, requests):
    answer = 0
    n, m = len(storage), len(storage[0]) # 세로, 가로
    outside = [[False] * (m + 2) for _ in range(n + 2)] # [i][j]: 창고 외부 영역 True/False
    removed = [[False] * m for _ in range(n)] # [i][j]: 컨테이너 제거 여부
    
    # 창고 외부 접촉 여부 초기화
    for i in range(n + 2):
        if i == 0 or i == n + 1:
            for j in range(m + 2):
                outside[i][j] = True
        else:
            outside[i][0] = True
            outside[i][-1] = True
            
    def is_accessible(x, y):
        for i in range(4):
            # 4면 중 하나가 외부와 연결되는 경우
            if outside[x + dx[i]][y + dy[i]]:
                return True
        return False
    
    # 외부 영역 갱신
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        outside[x + 1][y + 1] = True
        while queue:
            curr_x, curr_y = queue.popleft()
            for i in range(4):
                new_x = curr_x + dx[i]
                new_y = curr_y + dy[i]
                if 0 <= new_x < n and 0 <= new_y < m:
                    if not outside[new_x + 1][new_y + 1] and removed[new_x][new_y]:
                        queue.append((new_x, new_y))
                        outside[new_x + 1][new_y + 1] = True
                        
    for request in requests:
        target = request[0]       
        queue = deque()
        # 요청 길이 1: 지게차 사용
        if len(request) == 1:
            for i in range(n):
                for j in range(m):
                    if not removed[i][j] and storage[i][j] == target:
                        if is_accessible(i + 1, j + 1):
                            queue.append((i, j))

        # 요청 길이 2: 크레인 사용
        else:
            for i in range(n):
                for j in range(m):
                    if not removed[i][j] and storage[i][j] == target:  
                        queue.append((i, j))
                        
        # 하나의 요청은 한번에 처리. 영역 갱신이 서로 영향이 가지 않도록
        while queue:
            x, y = queue.popleft()
            answer += 1
            removed[x][y] = True
            # 외부 접근 영역 갱신
            if is_accessible(x + 1, y + 1):
                bfs(x, y)
            
    return n * m - answer