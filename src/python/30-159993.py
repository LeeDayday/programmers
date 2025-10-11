# https://school.programmers.co.kr/learn/courses/30/lessons/159993
# 연습문제

# 시작 지점 > 레버 + 레버 > 출구의 최소 시간 구하기
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def solution(maps):
    answer = 0
    m, n = len(maps), len(maps[0]) # 미로의 세로, 가로 길이
        
    def bfs(start, end):
        visited = [[False] * n for _ in range(m)]
        queue = deque()
        # 출발 지점 방문 처리
        queue.append(start)
        visited[start[0]][start[1]] = 0
        
        while queue:
            curr_x, curr_y = queue.popleft()
            # 목표 지점에 도달한 경우 반복문 종료
            if curr_x == end[0] and curr_y == end[1]:
                break
                
            for i in range(4):
                new_x = curr_x + dx[i]
                new_y = curr_y + dy[i]
                if 0 <= new_x < m and 0 <= new_y < n:
                    # 방문한 적이 없고 벽이 아는 경우
                    if not visited[new_x][new_y] and maps[new_x][new_y] != 'X':
                        queue.append((new_x, new_y))
                        visited[new_x][new_y] = visited[curr_x][curr_y] + 1
        
        return visited[end[0]][end[1]] # 목표 지점까지 걸린 시간

    for i in range(m):
        for j in range(n):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                end = (i, j)

    # 시작 지점 > 레버 최소 시간
    result = bfs(start, lever)
    if result is False:
        return -1
    answer += result
    
    # 레버 > 도착 지점 최소 시간
    result = bfs(lever, end)
    if result is False:
        return -1
    answer += result
            
    return answer