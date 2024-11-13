# https://school.programmers.co.kr/learn/courses/30/lessons/42862
# 탐욕법

def solution(n, lost, reserve):
    # 중복 (도난 && 여벌 학생) 제거
    _reserve = set(reserve) - set(lost) # 여벌 옷이 있는 학생 집합
    lost = set(lost) - set(reserve) # 옷이 없는 학생 집합
    
    for r in sorted(_reserve):
        # 왼쪽 학생에게 빌려주기
        if r - 1 in lost:
            lost.discard(r - 1)
        # 오른쪽 학생에게 빌려주기
        elif r + 1 in lost:
            lost.discard(r + 1)
    
    return n - len(lost)