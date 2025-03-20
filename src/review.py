# 복습 - 뒤에 있는 큰 수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/154539

# O(N)

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = [] # 오큰수 update가 필요한 answer 의 index 저장
    
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    
    return answer