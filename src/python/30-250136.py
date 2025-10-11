# https://school.programmers.co.kr/learn/courses/30/lessons/250136
# PCCP 기출문제

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def solution(land):
    n = len(land) # 세로
    m = len(land[0]) # 가로
    answer = [0] * (m) # column별 총 석유량
    visited = [[False for _ in range(m)] for _ in range(n)] # 방문 여부
    
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        visited[x][y] = True
        cnt = 1
        cols = set()
        while queue:
            curr_x, curr_y = queue.popleft()
            cols.add(curr_y)
            for i in range(4):
                new_x = curr_x + dx[i]
                new_y = curr_y + dy[i]
                if 0 <= new_x < n and 0 <= new_y < m:
                    if land[new_x][new_y] == 1 and not visited[new_x][new_y]:
                        queue.append((new_x, new_y))
                        visited[new_x][new_y] = True
                        cnt += 1
                        
        for col in cols:
            answer[col] += cnt
    
        
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j] == 1:
                bfs(i, j)
                
    return max(answer)