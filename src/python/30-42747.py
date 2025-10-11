# https://school.programmers.co.kr/learn/courses/30/lessons/42747
# 정렬

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    
    for i in range(len(citations)):
        # citations[i]: 인용된 횟수 (=h)
        # i + 1: h번 인용된 논문 편 수
        if citations[i] < i + 1:
            return i

    return len(citations)    