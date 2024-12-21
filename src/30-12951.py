# https://school.programmers.co.kr/learn/courses/30/lessons/12951
# 연습문제

def solution(s):
    answer = ''
    flag = True # 대문자

    for ch in s:
        # 공백인 경우
        if ch == ' ':
            answer += ' '
            flag = True     
        elif flag:
            answer += ch.upper() # 알파벳은 대문자로, 숫자는 그대로
            flag = False
        else:
            answer += ch.lower() # 알파벳은 소문자로, 숫자는 그대로

    return answer