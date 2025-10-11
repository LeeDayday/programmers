# https://school.programmers.co.kr/learn/courses/30/lessons/43165
# 깊이/너비 우선 탐색 (DFS/BFS)

def solution(numbers, target):
    answer = [0]
    def dfs(idx, result): # idx: 접근할 numbers의 index, result: 누적값
        if idx == len(numbers):
            if result == target:
                answer[0] += 1
                return
            else:
                return
        dfs(idx + 1, result + numbers[idx])
        dfs(idx + 1, result - numbers[idx])
        return
    
    dfs(0, 0)
    return answer[0]
