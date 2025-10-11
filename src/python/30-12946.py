# https://school.programmers.co.kr/learn/courses/30/lessons/12946
# 하노이의 탑

def solution(n):
    answer = [] # 최종 결과

    def hanoi(n, start, end, extra): 
        '''
        원판 개수, 시작 기둥, 목표 기둥, 보조 기둥
        '''
        if n == 1:
            answer.append([start + 1, end + 1])
            return
        else:
            # 가장 큰 원판을 목표 기둥으로 옮기기 위해선
            # 나머지 n - 1개의 원판을 보조 기둥으로 옮겨야 함
            hanoi(n - 1, start, extra, end) # n - 1개 보조 기둥으로 옮기기
            answer.append([start + 1, end + 1]) # 가장 큰 원판을 목표 기둥으로 옮기기
            hanoi(n - 1, extra, end, start) # n - 1개 목표 기둥으로 옮기기
    
    hanoi(n, 0, 2, 1)
    return answer