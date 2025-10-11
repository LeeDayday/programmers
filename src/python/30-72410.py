# https://school.programmers.co.kr/learn/courses/30/lessons/72410
# 2021 KAKAO BLIND RECRUITMENT

import re
def clean_id(input_id):
    pattern = r'[^0-9a-z\-\_\.]'
    return re.sub(pattern, '', input_id)

def solution(new_id):
    answer = ''
    
    # step 1: 소문자 치환
    answer = new_id.lower()
    # step 2: 특수문자 제거
    answer = clean_id(answer)
    # step 3: 중복된 마침표 치환
    answer = re.sub('\.{2,}', '.', answer)
    # step 4: 처음 / 끝 마침표 제거
    answer = answer.lstrip('.').rstrip('.')
    # step 5: 빈 문자열 처리
    if len(answer) == 0:
        answer += 'a'
    # step 6: 16자 이상인 경우
    if len(answer) >= 16:
        answer = answer[:15]
        answer = answer.lstrip('.').rstrip('.')
    # step 7: 2자 이하인 경우
    while len(answer) <= 2:
        answer += answer[-1]
    return answer