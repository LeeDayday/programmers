# 복습 - 아이템 줍기
# https://school.programmers.co.kr/learn/courses/30/lessons/87694

# O(V + E) (V: 테두리 위에 있는 좌표 수)

from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def solution(rectangle, characterX, characterY, itemX, itemY):
    
    def bfs(graph):
        queue = deque()
        visited = [[-1] * (102) for _ in range(102)]
        queue.append((characterX * 2, characterY * 2))
        visited[characterX * 2][characterY * 2] = 0
        while queue:
            curr_x, curr_y = queue.popleft()
            if curr_x == itemX * 2 and curr_y == itemY * 2:
                break
            for i in range(4):
                new_x = curr_x + dx[i]
                new_y = curr_y + dy[i]
                if 0 <= new_x < len(visited[0]) and 0 <= new_y < len(visited):
                    if graph[new_x][new_y] == 1 and visited[new_x][new_y] == -1:
                        visited[new_x][new_y] = visited[curr_x][curr_y] + 1
                        queue.append((new_x, new_y))
                        
        return visited[itemX * 2][itemY * 2] // 2
        
    answer = 0
    # 명확한 동서남북 이동을 위해 그래프 2배 확장
    graph = [[-1] * (102) for _ in range(102)] # -1: 미방문, 0: 내부, 1: 테두리
    
    for start_x, start_y, end_x, end_y in rectangle:
        for x in range(start_x * 2, end_x * 2 + 1):
            for y in range(start_y * 2, end_y * 2 + 1):
                # 내부 영역은 기존 직사각형 상관없이 무조건 내부 영역으로 표시
                if start_x * 2 < x < end_x * 2 and start_y * 2 < y < end_y * 2:
                    graph[x][y] = 0
                # 기존에 내부로 표시되지 않은 경우에만 테두리 표시
                else:
                    if graph[x][y] != 0:
                        graph[x][y] = 1

    return bfs(graph)