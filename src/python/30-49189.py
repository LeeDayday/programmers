# https://school.programmers.co.kr/learn/courses/30/lessons/49189
# 그래프

from collections import defaultdict
from heapq import heappush, heappop
INF = int(1e9)

def solution(n, edge):
    answer = 0
    graph = defaultdict(list)
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)
    
    distance = [INF] * (n + 1) # 1번 노드로부터의 최소 거리 (거리: 간선의 개수)
    distance[1] = 0 # 1번 노드 거리 초기화
    heap = []

    def dijkstra(node):
        heappush(heap, (distance[node], node))
            
        while heap:
            curr_dis, curr_node = heappop(heap)
            for new_node in graph[curr_node]:
                if distance[new_node] > distance[curr_node] + 1: # 거리 업데이트가 필요한 경우
                    distance[new_node] = distance[curr_node] + 1
                    heappush(heap, (distance[new_node], new_node))
                    
    dijkstra(1)
    max_d = 0
    for i in range(1, n + 1):
        if max_d < distance[i]:
            max_d = distance[i]
            answer = 1
        elif max_d == distance[i]:
            answer += 1
            
    return answer