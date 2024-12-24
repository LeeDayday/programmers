# https://school.programmers.co.kr/learn/courses/30/lessons/12945
# 연습문제

def solution(n):
    if n <= 2:
        return 1
    else:
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = (dp[i - 2] + dp[i - 1]) % 1234567
    return dp[-1]