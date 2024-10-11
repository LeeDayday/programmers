# https://school.programmers.co.kr/learn/courses/30/lessons/72413
# 2021 카카오 블라인드 채용


from heapq import heappush, heappop
INF = int(1e9)

def dijkstra(graph, n, start, end):
    result = [INF] * (n + 1) # start을 기준으로 각 정점까지의 최소 비용 리스트
    result[start] = 0
    
    heap = []
    heappush(heap, (0, start))
    
    while heap:
        cost, node = heappop(heap)
        # 비용 업데이트 여부
        if result[node] < cost:
            continue
        # node를 거쳐 갔을 때의 비용 비교
        for i in range(1, n + 1):
            # start -> i vs start -> node -> i
            if result[i] > cost + graph[node][i]:
                result[i] = cost + graph[node][i]
                heappush(heap, (cost + graph[node][i], i))
    
    return result[end]
        
    
def solution(n, s, a, b, fares):
    graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)] # 인접 리스트
    # 인접 리스트 생성
    for c, d, f in fares:
        graph[c][d] = f
        graph[d][c] = f
    
    # 합승을 전혀 하지 않는 경우 (s->a + s->b)
    result1 = dijkstra(graph, n, s, a) + dijkstra(graph, n, s, b)

    result2 = INF
    # 합승을 하는 경우
    for i in range(1, n + 1):
        # i 번 정점까지 합승, 그 이후 각자
        result2 = min(result2, dijkstra(graph, n, s, i) + dijkstra(graph, n, i, a) + dijkstra(graph, n, i, b))
    
    
    return min(result1, result2)