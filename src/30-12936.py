# https://school.programmers.co.kr/learn/courses/30/lessons/12936
# 줄 서는 방법
from math import factorial, ceil
    
def solution(n, k):
    answer = []
    data = [i for i in range(1, n + 1)]
    def get_answer(a, k):
        if a == 0:
            return
        num = factorial(a - 1)
        index = (k - 1) // num
        answer.append(data.pop(index))
        get_answer(a - 1, k - index * num)
    
    get_answer(n, k)
    return answer

