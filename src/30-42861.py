# https://school.programmers.co.kr/learn/courses/30/lessons/42861
# 탐욕법

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x

def solution(n, costs):
    # 비용 오름차순 정렬
    costs.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]
    answer = 0 # 총 다리 건설 비용
    
    for cost in costs:
        s, e, w = cost
              
        if find_parent(parent, s) != find_parent(parent, e):
            union(parent, s, e)
            answer += w        
    
    return answer