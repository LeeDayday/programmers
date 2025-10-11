# https://school.programmers.co.kr/learn/courses/30/lessons/87946
# 완전탐색

answer = 0
def dfs(k, visited_cnt, dungeons, visited):
    global answer
    if visited_cnt > answer:
        answer = visited_cnt
    
    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k - dungeons[i][1], visited_cnt + 1, dungeons, visited)
            visited[i] = False
        
def solution(k, dungeons):
    global answer
    visited = [False] * len(dungeons)
    dfs(k, 0, dungeons, visited)
    return answer