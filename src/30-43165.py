# https://school.programmers.co.kr/learn/courses/30/lessons/43165
# 깊이/너비 우선 탐색 (DFS/BFS)

def solution(numbers, target):
    answer = 0
    
    def get_cnt(start):
        dp = [[0] * (2 ** row) for row in range(len(numbers))]
        dp[0][0] = start
        for i in range(1, len(numbers)):
            for j in range(0, 2 ** i, 2):
                dp[i][j] = dp[i - 1][j // 2] + numbers[i]
                dp[i][j + 1] = dp[i - 1][j // 2] - numbers[i]
        
        cnt = 0
        for num in dp[-1]:
            if num == target:
                cnt += 1
                
        return cnt
                
    answer += get_cnt(numbers[0])
    answer += get_cnt(-numbers[0])
    return answer