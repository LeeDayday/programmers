# https://school.programmers.co.kr/learn/courses/30/lessons/172927
# 연습문제

fatigue_values = {"diamond": (1, 1, 1), "iron": (5, 1, 1), "stone": (25, 5, 1)} # key: 곡괭이, value: 광물 별 피로도
indexes= {'diamond': 0, 'iron': 1, 'stone': 2}
def dfs(picks, minerals, index, fatigue):
    global min_fatigue

    # 모든 광물을 캤거나, 더 사용할 곡괭이가 없을 때 종료
    if sum(picks) == 0 or index >= len(minerals):
        min_fatigue = min(min_fatigue, fatigue)
        return

    # 현재까지의 피로도가 최소 피로도보다 크다면 탐색 중단
    if fatigue >= min_fatigue:
        return

    # 현재 위치에서 곡괭이 선택
    for i, pick in enumerate(["diamond", "iron", "stone"]):
        if picks[i] > 0:  # 해당 곡괭이가 남아있을 때만 사용 가능
            picks[i] -= 1  # 곡괭이 사용

            # 5개 단위로 광물 캐기
            new_fatigue = 0
            for j in range(5):
                if index + j >= len(minerals):  # 범위를 초과하면 종료
                    break
                mineral = minerals[index + j]
                new_fatigue += fatigue_values[pick][indexes[mineral]]

            # 다음 탐색
            dfs(picks, minerals, index + 5, fatigue + new_fatigue)

            picks[i] += 1  # 백트래킹: 곡괭이 개수 복구

def solution(picks, minerals):
    global min_fatigue

    min_fatigue = float('inf')

    dfs(picks, minerals, 0, 0)  # 곡괭이 리스트, 광물 리스트, 광물 index, 누적 피로도

    return min_fatigue
