# https://school.programmers.co.kr/learn/courses/30/lessons/42862
# 탐욕법

def solution(n, lost, reserve):
    answer = 0
    clothes_dict = {i: 1 for i in range(1, n + 1)} # 학생 번호: 체육복 수 dict
    # 체육복 없는 학생
    for num in lost:
        clothes_dict[num] -= 1
        
    # 체육복 여벌 학생
    for num in reserve:
        clothes_dict[num] += 1

    for i in range(1, n + 1):
        # 체육복이 없는 경우
        if clothes_dict[i] == 0:
            # 왼쪽 검사
            if i > 1 and clothes_dict[i - 1] > 1:
                # 왼쪽에서 빌려오기
                clothes_dict[i - 1] -= 1
                clothes_dict[i] += 1
                continue
            # 오른쪽 검사
            if i + 1 <= n and clothes_dict[i + 1] > 1:
                # 오른쪽에서 빌려오기
                clothes_dict[i + 1] -= 1
                clothes_dict[i] += 1

    # 체육복이 있는 인원 계산
    for i in range(1, n + 1):
        if clothes_dict[i] > 0:
            answer += 1
    
            
    return answer