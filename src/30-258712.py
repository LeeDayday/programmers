# https://school.programmers.co.kr/learn/courses/30/lessons/258712
# 2024 카카오 개발자 겨울 인턴십


def solution(friends, gifts):
    answer = 0
    friend_cnt = len(friends)
    present = [[False for _ in range(friend_cnt + 1)] for _ in range(friend_cnt)] # 선물 지수를 표현한 이차원 배열
    friend_dict = {} # 친구 이름과 idx를 관리하는 dictionary
    for i, friend in enumerate(friends):
        friend_dict[friend] = i
        
    for gift in gifts:
        give, take = gift.split(" ")
        give_idx = friend_dict.get(give)
        take_idx = friend_dict.get(take)
        if present[give_idx][take_idx] is False:
            present[give_idx][take_idx] = 0
            present[take_idx][give_idx] = 0
        present[give_idx][take_idx] += 1
        present[take_idx][give_idx] -= 1
        
    for i in range(friend_cnt):
        cnt = 0 # 친구 별 선물 지수 계산
        for j in range(friend_cnt):
            if present[i][j] != False:
                cnt += present[i][j]
        present[i][-1] = cnt
            
    result = [0 for _ in range(friend_cnt)] 
    for i in range(friend_cnt):
        for j in range(friend_cnt):
            if i == j:
                continue
            # 두 사람이 선물을 주고 받은 기록이 있다면
            if present[i][j] != False and present[i][j] > 0:
                # 더 많은 선물을 준 사람이 다음 달에 받는다
                result[i] += 1
                continue
            # 주고 받은 기록이 없거나 주고받은 수가 같다면
            if present[i][j] is False or present[i][j] == 0:
                # 선물 지수가 더 큰 사람이 받는다
                if present[i][-1] > present[j][-1]:
                    result[i] += 1
                # 선물 지수가 같은 경우 선물을 주고받지 않는다
                elif present[i][-1] == present[j][-1]:
                    continue
                    
    print(result)
    answer = max(result)
    
    return answer