# https://school.programmers.co.kr/learn/courses/30/lessons/68936
# 월간 코드 챌린지 시즌 1

dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]


def solution(arr):
    answer = [0, 0] # 0의 개수, 1의 개수
    N = len(arr) # 한 변의 길이

    # 압축 수행
    def get_cnt(i, j, n, answer, arr):
        # basecase: 더 이상 압축이 불가능한 경우
        if n == 0:
            answer[arr[i][j]] += 1
            return
        flag = arr[i][j] # 비교 기준
        for x in range(i, i + n):
            for y in range(j, j + n):
                if flag != arr[x][y]: # 기준과 값이 다른 경우: 압축이 필요한 경우
                    for k in range(4):
                        get_cnt(i + dx[k] * (n // 2), j + dy[k] * (n // 2), n // 2, answer, arr)          
                    return
        answer[flag] += 1
        return
    
    # 압축 수행
    for i in range(4):
        get_cnt(0 + dx[i] * (N // 2), 0 + dy[i] * (N // 2), N // 2, answer, arr)

    if answer[0] == 4 and answer[1] == 0:
        answer[0] = 1
    elif answer[0] == 0 and answer[1] == 4:
        answer[1] = 1
    return answer