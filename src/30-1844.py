# https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 깊이/너비 우선 탐색(DFS/BFS)

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def solution(maps):
    answer = 0
    
    def bfs(n, m):
        result = [[-1] * m for _ in range(n)]
        queue = deque()
        result[0][0] = 1
        queue.append((0, 0))
        
        while queue:
            curr_x, curr_y = queue.popleft()
            for i in range(4):
                new_x = curr_x + dx[i]
                new_y = curr_y + dy[i]
                # new_x, new_y가 maps 범위 내에 존재
                if 0 <= new_x < n and 0 <= new_y < m:
                    # 해당 위치가 벽이 아니고 방문 가능한 경우
                    if result[new_x][new_y] == -1 and maps[new_x][new_y] == 1:
                        result[new_x][new_y] = result[curr_x][curr_y] + 1
                        queue.append((new_x, new_y))
        
        return result[-1][-1]
    
    answer = bfs(len(maps), len(maps[0])) # n x m
    return answer