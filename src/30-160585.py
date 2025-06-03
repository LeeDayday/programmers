# https://school.programmers.co.kr/learn/courses/30/lessons/160585
# 연습문제

def is_finished(board, player):

    for i in range(3):
        if board[i][0] == player and (board[i][0] == board[i][1] == board[i][2]):
            return True
        if board[0][i] == player and (board[0][i] == board[1][i] == board[2][i]):
            return True
                
    if board[0][0] == player and (board[0][0] == board[1][1] == board[2][2]):
        return True
            
    if board[0][2] == player and (board[0][2] == board[1][1] == board[2][0]):
        return True
            
    return False

def solution(board):
    answer = -1
    cnt = [0, 0] # (O, X) 의 개수
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                cnt[0] += 1
            elif board[i][j] == 'X':
                cnt[1] += 1
    
    result = [False, False]
    result[0] = is_finished(board, 'O')
    result[1] = is_finished(board, 'X')
    
    if cnt[0] == cnt[1]:
        if not result[0]:
            return 1
    if cnt[0] == cnt[1] + 1:
        if not result[1]:
            return 1

    return 0
