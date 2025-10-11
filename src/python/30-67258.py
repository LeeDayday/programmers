# https://school.programmers.co.kr/learn/courses/30/lessons/67258
# 2020 카카오 인턴십십

from collections import  defaultdict
def solution(gems):
    n = len(gems) # 진열대 총 길이
    cnt = len(set(gems)) # 총 보석 개수
    min_length = int(1e9) # 조건을 만족하는 범위의 최소 길이
    
    visited = defaultdict(int) # key: 보석 종류, value: 구매한 개수
    start, end = 0, 0
    s_result, e_result = 0, 0 # 최종 결과값
    
    while end < n:
        # 보석 추가
        visited[gems[end]] += 1
        end += 1
        # 모든 종류의 보석을 구매한 경우, start 이동
        while len(visited) == cnt:
            if min_length > end - start:
                s_result = start + 1
                e_result = end
                min_length = end - start
            # start 이동
            visited[gems[start]] -= 1
            if visited[gems[start]] == 0:
                del visited[gems[start]]
            start += 1
    return [s_result, e_result]