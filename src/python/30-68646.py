# https://school.programmers.co.kr/learn/courses/30/lessons/68646
# 월간 코드 챌린지 시즌1


def solution(a):
    answer = 0
    n = len(a)
    
    if n <= 2:
        return n
    
    # 각 위치에서 살아남을 수 있는 가장 작은 풍선 리스트
    left_min = [0] * n # 왼쪽부터 탐색했을 때, 최솟값
    right_min = [0] * n # 오른쪽부터 탐색했을 때, 최솟값
    
    # 왼쪽에서부터 최솟값 저장
    left_min[0] = a[0]
    for i in range(1, n):
        left_min[i] = min(left_min[i - 1], a[i])  # 왼쪽에서의 최소값 갱신

    # 오른쪽에서부터 최솟값 저장
    right_min[-1] = a[-1]
    for i in range(n - 2, -1, -1):
        right_min[i] = min(right_min[i + 1], a[i])  # 오른쪽에서의 최소값 갱신

    for i in range(n):
        if (a[i] == left_min[i]) or (a[i] == right_min[i]):
            answer += 1
            
    return answer