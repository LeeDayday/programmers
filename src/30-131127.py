# https://school.programmers.co.kr/learn/courses/30/lessons/131127
# 연습문제

def solution(want, number, discount):
    answer = 0
    data = dict()
    for i in range(len(want)):
        data[want[i]] = number[i]

    for i in range(len(discount) - 9):
        tmp_answer = 0
        tmp_data = data.copy()
        
        for name in discount[i:i+10]:
            if name in tmp_data.keys():
                if tmp_data[name] > 0:
                    tmp_data[name] -= 1
                    tmp_answer += 1
                    
        if tmp_answer == 10:
            answer += 1

    return answer