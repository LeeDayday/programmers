# https://school.programmers.co.kr/learn/courses/30/lessons/49191
# 그래프

def solution(n, results):
    answer = 0
    graph = [[-1 for _ in range(n + 1)] for _ in range(n + 1)] #[i][j] = 1: i가 j를 이긴다
    
    for i in range(n + 1):
        graph[i][i] = 1 # 자기 자신에 대한 승패는 고려 x
        
    for a, b in results:
        graph[a][b] = 1
        graph[b][a] = 0
        
    for k in range(1, n + 1): # 경유
        for i in range(1, n + 1): # 출발
            for j in range(1, n + 1): # 도착
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                elif graph[i][k] == 0 and graph[k][j] == 0:
                    graph[i][j] = 0
                    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] == -1: # 순위를 알 수 없는 경우
                break
        else: # break 없이 for문을 모두 돈 경우
             answer += 1   
    
    return answer