# https://school.programmers.co.kr/learn/courses/30/lessons/43162
# 깊이/너비 우선 탐색 (DFS/BFS)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
def solution(n, computers):
    answer = 0
    parent = [v for v in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                union_parent(parent, i, j)
                
    # 마지막으로 모든 정점에 대한 루트 노드 갱신
    for i in range(n):
        parent[i] = find_parent(parent, i)

    return len(set(parent))