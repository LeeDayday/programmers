# https://school.programmers.co.kr/learn/courses/30/lessons/43163
# 깊이/너비 우선 탐색 (DFS/BFS)

from collections import deque

def solution(begin, target, words):
    queue = deque()
    queue.append((begin, 0)) # (단어, 경로)
    visited = [False] * (len(words)) # 방문 여부
    
    while queue:
        curr_word, curr_cnt = queue.popleft()
        if curr_word == target:
            return curr_cnt
        for i in range(len(words)):
            if not visited[i]: # 방문하지 않은 단어인 경우, 단어 한 자씩 비교
                tmp = 0
                for j in range(len(curr_word)):
                    if words[i][j] != curr_word[j]:
                        tmp += 1
                if len(words[i]) == len(curr_word) and tmp == 1: # 한 글자만 다른 경우
                    queue.append((words[i], curr_cnt + 1))
                    visited[i] = True
                        
                
    return 0