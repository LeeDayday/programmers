# https://school.programmers.co.kr/learn/courses/30/lessons/12905
# 연습문제

def solution(board):
    answer = 0
    m = len(board)
    n = len(board[0])
    
    dp = [[0] * n for _ in range(m)] # dp[i][j]: (i, j)에서 만들 수 있는 정사각형의 최대 길이
    
    # 초기 행,열 값 적용
    for i in range(n):
        dp[0][i] = board[0][i]
        answer = max(answer, dp[0][i])
    for i in range(m):
        dp[i][0] = board[i][0]
        answer = max(answer, dp[i][0])
        
    for i in range(1, m):
        for j in range(1, n):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j - 1], dp[i - 1][j]) + 1 # 왼쪽, 왼쪽 대각선 위, 위가 모두 1인지 
                answer = max(answer, dp[i][j])
    

    return answer ** 2
