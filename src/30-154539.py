# https://school.programmers.co.kr/learn/courses/30/lessons/154539
# 연습문제

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)

    return answer