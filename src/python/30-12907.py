# https://school.programmers.co.kr/learn/courses/30/lessons/12907
# 거스름돈돈

def solution(n, money):
    m = len(money)
    # dp[i][j]: i번째 동전까지 사용해서 금액 j를 만드는 경우의 수
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 초기화: i번째 동전까지 사용해서 금액 0을 만드는 경우의 수: 1가지
    for i in range(m + 1):
        dp[i][0] = 1

    for i in range(1, m + 1):       # 동전 인덱스 (1부터 시작)
        for j in range(1, n + 1):  # 목표 금액
            if j >= money[i - 1]: # i번째 동전을 사용할 수 있는 경우
                dp[i][j] = dp[i - 1][j] + dp[i][j - money[i - 1]]  # 동전을 사용하지 않는 경우 + 사용하는 경우
            else: # i번째 동전을 사용할 수 없는 경우
                dp[i][j] = dp[i - 1][j]  

    return dp[-1][-1]  # 최종 결과 반환