# https://school.programmers.co.kr/learn/courses/30/lessons/388352
# 2025 프로그래머스 코드챌린지 1차 예선

from itertools import combinations

def solution(n, q, ans):
    answer = 0
    result = set()
    m = len(q)
    for comb in combinations([i for i in range(1, n + 1)], 5):
        for idx in range(m):
            if len(set(comb) & set(q[idx])) == ans[idx]:
                continue
            else:
                break
        else:
            result.add(comb)
                        
    return len(result)