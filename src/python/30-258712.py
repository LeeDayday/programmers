# https://school.programmers.co.kr/learn/courses/30/lessons/258712
# 2024 카카오 개발자 겨울 인턴십


def solution(friends, gifts):
    f = {v: i for i, v in enumerate(friends)} # (이름-idx)
    l = len(friends) # 전체 친구 수
    p = [0] * l # 선물 지수
    answer = [0] * l 
    gr = [[0] * l for _ in range(l)] # 선물을 준 관계를 정리
    
    for gift in gifts:
        a, b = gift.split()
        gr[f[a]][f[b]] += 1
    
    for i in range(l):
        p[i] = sum(gr[i]) - sum([k[i] for k in gr])
    
    for i in range(l):
        for j in range(l):
            if gr[i][j] > gr[j][i]:
                answer[i] += 1
            elif gr[i][j] == gr[j][i]:
                if p[i] > p[j]:
                    answer[i] += 1
                    
    return max(answer)