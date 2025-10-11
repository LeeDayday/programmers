# https://school.programmers.co.kr/learn/courses/30/lessons/169199
# 연습문제

from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def solution(board):
    m = len(board)
    n = len(board[0])
    
    def bfs(start_x, start_y, end_x, end_y):
        queue = deque()
        queue.append((start_x, start_y))
        board[start_x][start_y] = 0
        while queue:
            curr_x, curr_y = queue.popleft()
            for i in range(4):
                new_x, new_y = curr_x, curr_y
                # 직진
                while True:
                    new_x += dx[i]
                    new_y += dy[i]
                    # board 범위를 벗어나는 경우
                    if not (0 <= new_x < m and 0 <= new_y < n):
                        new_x -= dx[i]
                        new_y -= dy[i]
                        break
                    # D를 만난 경우
                    if board[new_x][new_y] == 'D':
                        new_x -= dx[i]
                        new_y -= dy[i]
                        break
                # 처음 방문한 영역인 경우만 이동 횟수 처리
                if board[new_x][new_y] == '.':
                    board[new_x][new_y] = board[curr_x][curr_y] + 1
                    queue.append((new_x, new_y))
                elif board[new_x][new_y] == 'G':
                    return board[curr_x][curr_y] + 1
        return -1
    
    for i in range(m):
        board[i] = list(board[i])
        for j in range(n):
            if board[i][j] == 'R':
                r_x, r_y = i, j
            if board[i][j] == 'G':
                g_x, g_y = i, j

    return bfs(r_x, r_y, g_x, g_y)