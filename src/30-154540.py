# https://school.programmers.co.kr/learn/courses/30/lessons/154540
# 연습문제

# X: 바다, 숫자: 무인도 내 식량
from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def solution(maps):
    answer = []
    m = len(maps)
    n = len(maps[0])
    visited = [[False] * n for _ in range(m)]
    
    def bfs(x, y):
        queue = deque()
        total = 0
        
        queue.append((x, y))
        visited[x][y] = True
        total += int(maps[x][y])
        
        while queue:
            curr_x, curr_y = queue.popleft()
            for i in range(4):
                new_x, new_y = curr_x + dx[i], curr_y + dy[i]
                if 0 <= new_x < m and 0 <= new_y < n:
                    if maps[new_x][new_y] != 'X' and not visited[new_x][new_y]:
                        total += int(maps[new_x][new_y])
                        queue.append((new_x, new_y))
                        visited[new_x][new_y] = True
        return total
                
            
        
    for i in range(m):
        for j in range(n):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(bfs(i, j))
                
    
    if answer:
        answer.sort()
        return answer
    else:
        return [-1]