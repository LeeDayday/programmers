# https://school.programmers.co.kr/learn/courses/30/lessons/176962
# 연습문제

# 기존 문자열 "hh:mm" 4자리 정수 hhmm으로 표현 
# 시간 차이는 분 단위
def get_time_diff(start, end):
    result_h = end // 100 - start // 100
    result_m = end % 100 - start % 100
    if result_m < 0:
        result_m += 60
        result_h -= 1
    return result_h * 60 + result_m

def add_time(time, minutes):
    h = time // 100
    m = time % 100 + minutes
    if m >= 60:
        h += 1
        m -= 60
    return h * 100 + m

def solution(plans):
    answer = []
    # 시간 정수화
    for i in range(len(plans)):
        h, m = plans[i][1].split(":")
        plans[i][1] = int(h) * 100 + int(m)
        plans[i][2] = int(plans[i][2])
    
    plans.sort(key=lambda x: x[1]) # 시작 시간 순으로 정렬

    stack = [(0, plans[0][2])] # (idx, 남은 시간)
    curr_time = plans[0][1] # 현재 시각
    
    for i in range(1, len(plans)):
        next_start = plans[i][1]
        gap = get_time_diff(curr_time, next_start)

        # 시간 여유가 있는 동안 이전 작업들을 처리
        while stack and gap > 0:
            idx, remain = stack.pop()
            if remain <= gap:
                answer.append(plans[idx][0])
                gap -= remain
                curr_time = add_time(curr_time, remain)
            else:
                remain -= gap
                curr_time = add_time(curr_time, gap)
                stack.append((idx, remain))
                gap = 0

        # 새 작업 시작
        stack.append((i, plans[i][2]))
        curr_time = next_start
        
    while stack:
        answer.append(plans[stack.pop()[0]][0])
    
        
    return answer