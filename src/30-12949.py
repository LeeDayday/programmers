# https://school.programmers.co.kr/learn/courses/30/lessons/12949
# 연습문제

def solution(arr1, arr2):
    # arr1: a x b
    # arr2: b x c
    # answer: a x c
    a = len(arr1)
    b = len(arr1[0])
    c = len(arr2[0])
    
    answer = [[0 for _ in range(c)] for _ in range(a)]
    for i in range(a):
        for j in range(c):
            for k in range(b):
                answer[i][j] += arr1[i][k] * arr2[k][j]
                
    return answer


