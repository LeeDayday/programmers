# https://school.programmers.co.kr/learn/courses/30/lessons/64065
# 2019 카카오 개발자 겨울 인턴십


def get_length(lst):
    return len(lst)

def solution(s):
    answer = []
    total_list = []
    tmp_list = []
    
    i = 2
    num = 0
    while i < len(s) - 1:
        if s[i] == ',' or s[i] == '}':
            if num != 0:
                tmp_list.append(num)
            num = 0
            if s[i] == '}':
                total_list.append(tmp_list)
                tmp_list = []
                
        elif s[i] == '{':
            pass
        else:
            num *= 10
            num += int(s[i])
        i += 1

    total_list = sorted(total_list, key=get_length)
    
    for i in range(len(total_list)):
        tmp_list = total_list[i]
        for num in tmp_list:
            if num not in answer:
                answer.append(num)
    return answer