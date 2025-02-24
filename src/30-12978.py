# https://school.programmers.co.kr/learn/courses/30/lessons/12978
# Summer/Winter Coding(~2018)

from heapq import heappush, heappop

def solution(N, road, K):
    answer = 0
    graph = {k: [] for k in range(1, N + 1)}
    
    for start, end, weight in road:
        # 양방향 그래프
        graph[start].append((end, weight)) # (마을 번호, 거리)
        graph[end].append((start, weight))

    distance = [int(1e9)] * (N + 1) # 1번 마을로부터 최단 거리
    visited = [False] * (N + 1)
    distance[1] = 0 # 초기값 설정
    
    def dijkstra(node):
        heap = []
        heappush(heap, (0, node)) # (최단 거리, 마을 번호)
        
        while heap:
            curr_distance, curr_node = heappop(heap)
            if distance[curr_node] < curr_distance:
                continue
            for new_node, new_distance in graph[curr_node]:
                # (1번 -> new_node) > (1번 -> curr_node -> new_node)
                if distance[new_node] > curr_distance + new_distance:
                    distance[new_node] = curr_distance + new_distance
                    heappush(heap, (curr_distance + new_distance, new_node))
    
    dijkstra(1)
    for i in range(1, N + 1):
        if distance[i] <= K:
            answer += 1
    
    return answer