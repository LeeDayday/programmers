
# https://school.programmers.co.kr/learn/courses/30/lessons/43164
# 깊이/너비 우선 탐색(DFS/BFS)
from collections import defaultdict


def solution(tickets):
    answer = []
    graph = defaultdict(list)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
    
    for key in graph.keys():
        graph[key].sort(reverse=True) # pop 시간 효율성을 위해 알파벳 내림차순 정렬
    
    def dfs(node):
        while graph[node]:
            next_node = graph[node].pop()
            dfs(next_node)
        answer.append(node)

    # 시작점 ICN에서 탐색 시작
    dfs("ICN")
    return answer[::-1]
