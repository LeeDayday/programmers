# https://school.programmers.co.kr/learn/courses/30/lessons/42898
# 동적계획법(Dynamic Programming)

def solution(m, n, puddles):
    dp = [[-1] * (m) for _ in range(n)]
    dp[0][0] = 1
    
    # 웅덩이 위치 경우의 수 초기화
    for y, x in puddles:
        dp[x - 1][y - 1] = 0
    
    for i in range(n):
        for j in range(m):
            # 방문하지 않은 위치에 대해서만 경우의 수 계산
            if dp[i][j] == -1:
                if i == 0 :
                    dp[i][j] = dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
    return dp[-1][-1]