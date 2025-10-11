# https://school.programmers.co.kr/learn/courses/30/lessons/340213
# PCCP 기출문제

def get_limit_time(time):
    # 출근 인정 시간 커트라인 정수형으로 반환
    h = time // 100
    m = time % 100
    m += 10
    if m >= 60:
        h += 1
        m -= 60
    return h * 100 + m

def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(schedules)):
        # i번째 직원의 출근 시간 검사하기
        time = get_limit_time(schedules[i])
        print(time)
        for day in range(7):
            # 주말인 경우
            if (startday + day) % 7 == 6 or (startday + day) % 7 == 0:
                continue
            # 지각한 경우
            if timelogs[i][day] > time:
                break
        else:
            answer += 1
    
    return answer