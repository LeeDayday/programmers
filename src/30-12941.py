# https://school.programmers.co.kr/learn/courses/30/lessons/12941
# 연습문제

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        answer += A[i] * B[i]
    
    return answer