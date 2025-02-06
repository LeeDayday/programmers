# https://school.programmers.co.kr/learn/courses/30/lessons/17686
# 2018 KAKAO BLIND RECRUITMENT

import re

def solution(files):
    data = []  # (HEAD, NUMBER, TAIL, 원래 파일명)

    for file in files:
        # HEAD: 숫자를 제외한 문자
        # NUMBER: 1~5자리 숫자
        # TAIL: NUMBER 이후 모든 것
        match = re.match(r'([\D]+)(\d{1,5})(.*)', file)
        if match:
            HEAD, NUMBER, TAIL = match.groups()
            data.append((HEAD.lower(), int(NUMBER), file))  # 정렬을 위해 HEAD는 소문자로 변환, NUMBER는 정수 변환

    # 정렬 기준: HEAD 사전순 → NUMBER 숫자순 → 원래 입력 순서 유지
    data.sort(key=lambda x: (x[0], x[1]))

    # 원래 파일명만 반환
    return [item[2] for item in data]