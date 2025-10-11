# https://school.programmers.co.kr/learn/courses/30/lessons/64065
# 2019 카카오 개발자 겨울 인턴십


def solution(s):
    answer = []
    # 문자열 데이터로부터 튜플 단위 원소 데이터 가져오기 (숫자 + , 형태)
    data = s[2:-2].split('},{')
    # 튜플 길이 기준 오름차순 정렬
    data = sorted(data, key=lambda x:len(x))
    
    for item in data:
        # 쉼표 제거 및 원소 정수화
        item = list(map(int, item.split(',')))
        for value in item:
            if value not in answer:
                answer.append(value)
    return answer