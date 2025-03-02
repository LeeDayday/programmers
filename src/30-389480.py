# https://school.programmers.co.kr/learn/courses/30/lessons/389480
# 2025 프로그래머스 코드챌린지 2차 예선

def solution(info, n, m):
    k = len(info)  # 총 물건 개수
    min_value = int(1e9)  # A의 최소 흔적 값을 저장

    # 메모이제이션: 방문한 상태를 저장하는 딕셔너리
    dp = {}

    def dfs(x, cnt_a, cnt_b):
        nonlocal min_value
        
        # 종료 조건: 모든 물건을 탐색했을 때
        if x >= k:
            min_value = min(min_value, cnt_a)
            return

        # 이미 탐색한 상태라면 중복 계산 방지
        if (x, cnt_a, cnt_b) in dp:
            return
        dp[(x, cnt_a, cnt_b)] = True  # 방문 체크

        # 현재 최소값보다 크면 탐색 종료
        if cnt_a >= min_value:
            return
        
        # 도둑 A가 훔치는 경우
        if cnt_a + info[x][0] < n:
            dfs(x + 1, cnt_a + info[x][0], cnt_b)
        
        # 도둑 B가 훔치는 경우
        if cnt_b + info[x][1] < m:
            dfs(x + 1, cnt_a, cnt_b + info[x][1])

    # DFS 탐색 시작
    dfs(0, 0, 0)

    # 최솟값이 갱신되지 않았다면, A가 훔칠 수 없는 경우
    return -1 if min_value == int(1e9) else min_value
