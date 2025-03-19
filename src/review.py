# 복습 - 무인도 여행
# https://school.programmers.co.kr/learn/courses/30/lessons/154540

# O(NM + N log N) ≈ O(NM)
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def solution(maps):
    answer = []
    n, m = len(maps), len(maps[0])
    visited = [[False] * (m) for _ in range(n)]
    def bfs(x, y):
        result = 0
        queue = deque([(x, y)])
        visited[x][y] = True
        
        while queue:
            x, y = queue.popleft()
            result += int(maps[x][y])
            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if 0 <= new_x < n and 0 <= new_y < m:
                    if not visited[new_x][new_y] and maps[new_x][new_y] != 'X':
                        queue.append((new_x, new_y))
                        visited[new_x][new_y] = True
        
        return result
        
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maps[i][j] != 'X':
                answer.append(bfs(i, j))
                
    if len(answer) == 0:
        return [-1]
    answer.sort()
        
    return answer