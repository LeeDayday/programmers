# https://school.programmers.co.kr/learn/courses/30/lessons/42586
# 스택 / 큐

def get_days(days, progresses, speeds):
    for i in range(len(progresses)):
        left_progress = 100 - progresses[i]
        if left_progress % speeds[i]:
            days.append(left_progress // speeds[i] + 1)
        else:
            days.append(left_progress // speeds[i])

def solution(progresses, speeds):
    answer = []
    days = []
    get_days(days, progresses, speeds) # 각 기능 당 개발 완료 기간 구하기
    cnt = 0
    idx = 0
    while idx < len(progresses):
        for i in range(idx, len(progresses)):
            if days[idx] < days[i]:
                break
            cnt += 1
        answer.append(cnt)
        idx += cnt
        cnt = 0  
    return answer
