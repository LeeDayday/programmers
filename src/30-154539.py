# https://school.programmers.co.kr/learn/courses/30/lessons/154539
# 연습문제

def solution(numbers):
    answer = [-1]
    stack = [len(numbers) - 1]
    for i in range(len(numbers) - 2, -1, -1):
        if stack and numbers[i] < numbers[stack[-1]]:
            answer.append(numbers[stack[-1]])
            stack.append(i)
        else:
            if stack:
                while stack:
                    if numbers[i] < numbers[stack[-1]]:
                        answer.append(numbers[stack[-1]])
                        stack.append(i)
                        break
                    stack.pop()
                else:
                    answer.append(-1)
                    stack.append(i)
            else:
                answer.append(-1)
                stack.append(i)

    return answer[::-1]