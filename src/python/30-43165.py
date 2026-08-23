# https://school.programmers.co.kr/learn/courses/30/lessons/43165
# 깊이/너비 우선 탐색 (DFS/BFS)

def solution(numbers, target):
    n = len(numbers)
    def dfs(idx, total):
        # basecase: 모두 순회한 경우
        if idx == n:
            return 1 if total == target else 0
        
        return dfs(idx + 1, total + numbers[idx]) + dfs(idx + 1, total - numbers[idx])
    
    
    return dfs(0, 0)
