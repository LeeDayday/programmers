# https://school.programmers.co.kr/learn/courses/30/lessons/12987
# Summer/Winter Coding(~2018)

def solution(A, B):
    answer = 0
    n = len(A)
    idx = 0
    A.sort()
    B.sort()
    for i in range(n):
        while idx < n and A[i] >= B[idx]:
            idx += 1
        if idx >= n:
            break
        idx += 1
        answer += 1
    return answer