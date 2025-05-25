# 복습 - 광물 캐기
# https://school.programmers.co.kr/learn/courses/30/lessons/172927

# O(3^n), n: 곡괭이 개수

minerals_dict= {'diamond': 0, 'iron': 1, 'stone': 2}
fatigue_dict = {"diamond": (1, 1, 1), "iron": (5, 1, 1), "stone": (25, 5, 1)}

def dfs(picks, minerals, idx, fatigue):
    global min_fatigue

    # basecase: 모든 광물을 캤거나, 더 사용할 곡괭이가 없을 때 종료
    if idx >= len(minerals) or sum(picks) == 0:
        min_fatigue = min(min_fatigue, fatigue)
        return

    # 중간 종료 조건: 현재까지의 피로도가 최소 피로도보다 크다면 탐색 중단
    if fatigue >= min_fatigue:
        return

    # 현재 위치에서 곡괭이 선택
    for i, pick in enumerate(["diamond", "iron", "stone"]): # i: 곡괭이 index, pick: 곡괭이 종류
        if picks[i] > 0:  # 해당 곡괭이가 남아있을 때만 사용 가능
            picks[i] -= 1  # 곡괭이 사용

            # 5개 단위로 광물 캐기
            curr_fatigue = 0
            for j in range(5):
                if idx + j >= len(minerals):
                    break
                mineral = minerals[idx + j]
                curr_fatigue += fatigue_dict[pick][minerals_dict[mineral]]

            # 다음 탐색
            dfs(picks, minerals, idx + 5, fatigue + curr_fatigue)
            picks[i] += 1  

def solution(picks, minerals):
    global min_fatigue

    min_fatigue = float('inf')

    dfs(picks, minerals, 0, 0)  # 곡괭이 리스트, 광물 리스트, 광물 index, 누적 피로도

    return min_fatigue
