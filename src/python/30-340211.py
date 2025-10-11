# https://school.programmers.co.kr/learn/courses/30/lessons/340211
# PCCP 기출문제

from collections import defaultdict

def move(data, start, end, current_time, robot_id):
    start_x, start_y = start
    end_x, end_y = end
    time = current_time  # 현재 시간
    result = 0

    # 로봇 초기위치 충돌 고려
    if (start_x, start_y) in data[time]:
        is_collision, robot_ids = data[time][(start_x, start_y)]
        if robot_id not in robot_ids:  # 다른 로봇인지 확인
            if not is_collision:  # 아직 충돌 계산되지 않은 경우
                result += 1
                is_collision = True  # 충돌 기록
            robot_ids.add(robot_id)  # 로봇 추가
        data[time][(start_x, start_y)] = (is_collision, robot_ids)
    else:
        data[time][(start_x, start_y)] = (False, {robot_id})  # 초기값

    # 세로 이동
    while start_x != end_x:
        if start_x > end_x:
            next_position = start_x - 1, start_y      
        else:
            next_position = start_x + 1, start_y

        time += 1  # 시간 증가

        # 충돌 여부 확인
        if next_position in data[time]:
            is_collision, robot_ids = data[time][next_position]
            if robot_id not in robot_ids:  # 다른 로봇인지 확인
                if not is_collision:  # 아직 충돌 계산되지 않은 경우
                    result += 1
                    is_collision = True  # 충돌 기록
                robot_ids.add(robot_id)  # 로봇 추가
            data[time][next_position] = (is_collision, robot_ids)
        else:
            data[time][next_position] = (False, {robot_id})

        # 이동
        start_x, start_y = next_position

    # 가로 이동
    while start_y != end_y:
        if start_y > end_y:
            next_position = start_x, start_y - 1      
        else:
            next_position = start_x, start_y + 1

        time += 1  # 시간 증가

        # 충돌 여부 확인
        if next_position in data[time]:
            is_collision, robot_ids = data[time][next_position]
            if robot_id not in robot_ids:  # 다른 로봇인지 확인
                if not is_collision:  # 아직 충돌 계산되지 않은 경우
                    result += 1
                    is_collision = True  # 충돌 기록
                robot_ids.add(robot_id)  # 로봇 추가
            data[time][next_position] = (is_collision, robot_ids)
        else:
            data[time][next_position] = (False, {robot_id})

        # 이동
        start_x, start_y = next_position

    return result, time

def solution(points, routes):
    answer = 0
    # 로봇 초당 좌표 위치 및 부가 정보 저장
    # time: (x, y): (충돌 여부, 로봇 ID) 저장
    data = defaultdict(dict)  

    # 로봇이 이동하며 발생하는 충돌 계산
    for robot_id, route in enumerate(routes, start=1):
        current_time = 0
        for j in range(len(route) - 1):
            start = points[route[j] - 1]
            end = points[route[j + 1] - 1]
            result, current_time = move(data, start, end, current_time, robot_id)
            answer += result

    return answer