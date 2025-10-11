from collections import defaultdict, deque

def get_extra_node(indegree):
    min_key = 0
    min_value = float('inf')
    for key, value in indegree.items():
        if min_value > value:
            min_key = key
            min_value = value
    return min_key


def search_graph(graph, visited, node):
    # 막대형 그래프
    if len(graph[node]) == 0:
        return 2
    # 도넛 / 8자 그래프 
    queue = deque()
    queue.append(node)
    visited[node] = True
    cnt_node = 0
    cnt_edge = 0
    
    while queue:
        curr_node = queue.popleft()
        cnt_node += 1
        for new_node in graph[curr_node]:
            cnt_edge += 1
            if not visited[new_node]:
                queue.append(new_node)
        
    # 정점, 간선 개수로 도넛형 / 8자형 그래프 판단
    print(f"{node} 의 그래프: {cnt_node}, {cnt_edge}")
    # 도넛모양 그래프
    if cnt_node == cnt_edge:
        print("도넛")
        return 1
    print("8자")
    return 3

            
       

def solution(edges):
    answer = [0, 0, 0, 0]
    graph = defaultdict(list) # 인접 정점 저장
    visited = defaultdict(bool) # 정점 방문 여부
    indegree = defaultdict(int) # 진입 차수
    
    for start, end in edges:
        graph[start].append(end)
        visited[start] = False
        visited[end] = False
    
    for node in visited.keys():
        indegree[node] = 0 

    for node in graph:
        for next_node in graph[node]:
            indegree[next_node] += 1
    
    extra_node = get_extra_node(indegree)
    answer[0] = extra_node

    for next_node in graph[extra_node]:
        if not visited[next_node]:
            #print(search_graph(graph, visited, next_node))
            answer[search_graph(graph, visited, next_node)] += 1
    return answer
        
# [2, 1, 1, 0]
print(solution([[2, 3], [4, 3], [1, 1], [2, 1]]))
# [4, 0, 1, 2]
print(solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]))
