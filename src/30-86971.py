# https://school.programmers.co.kr/learn/courses/30/lessons/86971
# 완전탐색

from collections import defaultdict, deque


def solution(n, wires):
    answer = int(1e9)
    graph = defaultdict(list)
        
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
        
    # start, end 사이의 간선이 제거되었을 때, 분할된 전력망이 가지고 있는 |송전탑 개수 차이| 반환
    def get_cnt(start, end):
        cnt = 0
        visited = [False] * (n + 1)
        queue = deque()
        queue.append(start)
        
        while queue:
            curr_node = queue.popleft()
            visited[curr_node] = True
            cnt += 1
            for new_node in graph[curr_node]:
                if not visited[new_node] and new_node != end:
                    queue.append(new_node)
        return abs(n - cnt - cnt)
        
    
    for wire in wires:
        answer = min(answer, get_cnt(wire[0], wire[1]))
        
    return answer