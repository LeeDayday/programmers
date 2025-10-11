# https://school.programmers.co.kr/learn/courses/30/lessons/43105
# 동적 계획법

def solution(triangle):
    # 삼각형 높이
    n = len(triangle)
    
    # dp list 선언 (triangle과 크기가 같은 list)
    dp = [[-1] * len(row) for row in triangle]
    
    def dfs(x, y):
        # base case: 마지막 행에 도달한 경우, 해당 값 반환
        if x == n - 1:
            return triangle[x][y]
        
        # 이미 계산이 되었다면, 해당 값을 반환
        if dp[x][y] != -1:
            return dp[x][y]
        
        # 왼쪽, 아래 중 최댓값 취하여 dp[x][y] 갱신
        left = dfs(x + 1, y)
        right = dfs(x + 1, y + 1)
        
        dp[x][y] = triangle[x][y] + max(left, right)
        
        return dp[x][y]
        
    return dfs(0, 0)
        