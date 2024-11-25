# https://school.programmers.co.kr/learn/courses/30/lessons/87694
# 깊이/너비 우선 탐색(DFS/BFS)

from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def solution(rectangle, characterX, characterY, itemX, itemY):
    # graph가 가지는 의미
    # 1: 직사각형의 경계선    0: 직사각형의 내부 영역    -1: 아무 영역 X
    graph = [[-1 for _ in range(102)] for _ in range(102)]
    visited = [[-1 for _ in range(102)] for _ in range(102)]

    # 직사격형 경계가 밀집한 경우, bfs 혼선 발생
    # 이를 방지하기 위하여 기존 좌표 x 2
    for pos in rectangle:
        start_x, start_y, end_x, end_y = map(lambda x:x*2, pos)
        for i in range(start_x, end_x + 1):
            for j in range(start_y, end_y + 1):
                if start_x < i < end_x and start_y < j < end_y: # 경계선을 제외한 내부
                    graph[i][j] = 0
                elif graph[i][j] != 0:
                    graph[i][j] = 1

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        visited[x][y] = 0
        while queue:
            curr_x, curr_y = queue.popleft()

            for i in range(4):
                new_x = curr_x + dx[i]
                new_y = curr_y + dy[i]

                if new_x == itemX * 2 and new_y == itemY * 2:
                    return (visited[curr_x][curr_y] + 1) // 2
                if 0 <= new_x < 102 and 0 <= new_y < 102:
                    # 방문한 적 없는 경계선 영역에 대해서 bfs 수행
                    if visited[new_x][new_y] == -1 and graph[new_x][new_y] == 1:
                        queue.append((new_x, new_y))
                        visited[new_x][new_y] = visited[curr_x][curr_y] + 1
        return 0
    return bfs(characterX * 2, characterY * 2) 


