# https://school.programmers.co.kr/learn/courses/30/lessons/84512
# 완전탐색색

def solution(word):
    answer = 0
    data = ['A', 'E', 'I', 'O', 'U']
    num = [5**i for i in range(len(data))]
    
    for i in range(len(word)-1,-1,-1):
        idx = data.index(word[i])
        for j in range(5-i):
            answer += num[j]*idx
        answer += 1
    return answer