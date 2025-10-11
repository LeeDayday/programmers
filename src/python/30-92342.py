# https://school.programmers.co.kr/learn/courses/30/lessons/92342
# 2022 KAKAO BLIND RECRUITMENT

# k 점을 어피치가 a 발, 라이언이 b 발
# a >= b 인 경우, 어피치가 k 점을 가져간다
# a = b = 0 인 경우, 아무도 점수 x
# 최종 점수 어피치 >= 라이언일 경우, 어피치 승

# 최종 점수 계산
def get_result(apeach, lion):
    score_a, score_b = 0, 0
    for i in range(10):
        if apeach[i] == lion[i] == 0:
            continue
        if apeach[i] >= lion[i]:
            score_a += 10 - i
        else:
            score_b += 10 - i
    
    # 라이언이 이긴 경우, 점수 차 반환
    if score_a < score_b:
        return score_b - score_a
    return -1
        
def solution(n, apeach):
    # n: 화살의 개수
    # apeach: 어피치가 점수 별 쏜 화살 개수 (10점 ~ 0점)
    
    max_diff = -1
    answer = [-1]
    # idx 번째 점수
    def dfs(idx, remain, lion):
        
        nonlocal max_diff, answer
        # base case: 화살을 모두 쏜 경우 / 모든 점수판을 탐색한 경우
        if remain == 0 or idx == 11:
            # 남은 화살이 있는 경우, 0점에 몰아넣기
            if remain > 0:
                lion[10] += remain
            diff = get_result(apeach, lion)

            # 점수 차가 더 큰 경우의 화살 정보 저장
            if diff > max_diff:
                answer = lion[:]
                max_diff = diff

            # 점수 차가 같은 경우, 가장 낮은 점수를 더 많이 맞힌 경우의 화살 정보 저장
            elif diff == max_diff and diff != -1:
                for i in range(10, -1, -1):
                    if lion[i] > answer[i]:
                        answer = lion[:]
                        break
                    if lion[i] < answer[i]:
                        break
            # 0점에 몰아 넣은 화살 복구
            if remain > 0:
                lion[10] -= remain
            return
                    
        # idx 번째 점수 획득
        if remain > apeach[idx]:
            # 화살 쏘기
            lion[idx] = apeach[idx] + 1
            dfs(idx + 1, remain - lion[idx], lion)
            # 원위치
            lion[idx] = 0
            
        # idx 번째 점수 포기
        dfs(idx + 1, remain, lion)
    
    dfs(0, n, [0] * 11)
    return answer

