# https://school.programmers.co.kr/learn/courses/30/lessons/92341
# 2022 KAKAO BLIND RECRUITMENT

from collections import defaultdict

# 총 주차 시간
def get_total_min(start, end):
    s_hour, s_min = (start.split(":"))
    e_hour, e_min = (end.split(":"))
    
    hours = int(e_hour) - int(s_hour)
    minutes = int(e_min) - int(s_min)
    
    if minutes < 0:
        hours -= 1
        minutes += 60
        
    return hours * 60 + minutes

def get_fee(fees, total):
    result = fees[1]
    total -= fees[0]
    while total > 0:
        total -= fees[2]
        result += fees[3]
    return result

def solution(fees, records):
    answer = []
    data = defaultdict(list)
    
    for record in records:
        time, id, in_out = record.split()
        data[id].append(time)
        
    id_list = list(data.keys())
    id_list.sort() # 차량 번호 오름차순 정렬
    
    for id in id_list:
        idx = 0
        total = 0
        while idx < len(data[id]):
            # 입차 & 출차
            if idx + 1 < len(data[id]):
                total += get_total_min(data[id][idx], data[id][idx + 1])
            # only 입차 (23:59 출차 간주)
            else:
                total += get_total_min(data[id][idx], "23:59")    
            idx += 2
        answer.append(get_fee(fees, total))

    return answer