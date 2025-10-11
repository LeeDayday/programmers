# https://school.programmers.co.kr/learn/courses/30/lessons/64064
# 2019 카카오 개발자 겨울 인턴십

import re
from itertools import permutations

def solution(user_id, banned_id):
    answer = 0
    result = []
    for perm in permutations(user_id, len(banned_id)):
        cnt = 0
        for i in range(len(perm)):
            ban = banned_id[i].replace('*', '.') # 정규 표현식에서 . 은 임의의 문자를 의미
            if re.fullmatch(ban,perm[i]):
                cnt += 1
        if cnt == len(banned_id):
            perm = sorted(perm)
            if perm not in result:
                result.append(perm)
                
    answer = len(result)
    
    return answer