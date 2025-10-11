# https://school.programmers.co.kr/learn/courses/30/lessons/68645
# 월간 코드 챌린지 시즌 1


dx = [1, 0, -1] 
dy = [0, 1, -1]

def solution(n):
    answer = []
    result = [[0] * row for row in range(1, n + 1)]
    result[0][0] = 1
    i, j = 0, 0
    k = 0
    total = (n * (n + 1)) // 2 # 전채 칸 수
    cnt = 1 # 값이 채워진 칸 수
    while cnt < total:
    
        new_i = i + dx[k]
        new_j = j + dy[k]
        if 0 <= new_i < n and 0 <= new_j <= i:
            # 칸 채우기
            if result[new_i][new_j] == 0:
                result[new_i][new_j] = result[i][j] + 1
                i, j = new_i, new_j
                cnt += 1
            # 달팽이 채우기 진행 방향 바꾸기
            else:
                k = (k + 1) % 3
        # 달팽이 채우기 진행 방향 바꾸기
        else:
            k = (k + 1) % 3
        
    # 최종 배열 구성
    for i in range(n):
        for j in range(i + 1):
            answer.append(result[i][j])
        
    return answer