# https://school.programmers.co.kr/learn/courses/30/lessons/42861
# 탐욕법

from heapq import heappush, heappop
from collections import defaultdict

def solution(n, costs):
    answer = 0
    visited = [False] * n

    graph = defaultdict(list)
    for start, end, weight in costs:
        graph[start].append((end, weight))
        graph[end].append((start, weight))
    
    heap = []
    heappush(heap, (0, 0)) # 초기 시작 노드, (weight, node)으로 heappush

    while heap:
        curr_weight, curr_node = heappop(heap)
        
        if not visited[curr_node]:
            answer += curr_weight
            visited[curr_node] = True

        for new_node, new_weight in graph[curr_node]:
            if not visited[new_node]:
                heappush(heap, (new_weight, new_node))

    return answer
