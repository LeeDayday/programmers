# https://school.programmers.co.kr/learn/courses/30/lessons/72411
# 메뉴 리뉴얼

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    # k개의 메뉴 조합 구하기
    for k in course:
        candidates = []
        for order in orders:
            # order 내 k 개의 메뉴 조합 탐색
            for comb in combinations(order, k):
                res = ''.join(sorted(comb)) # 메뉴 또한 오름차순
                candidates.append(res)
                
        # max_candidates: 가능한 k 개의 메뉴 조합 중 가장 많은 구성들
        max_candidates = Counter(candidates).most_common()
        for menu, cnt in max_candidates:
            if cnt > 1 and cnt == max_candidates[0][1]:
                answer.append(menu)
        
    return sorted(answer)