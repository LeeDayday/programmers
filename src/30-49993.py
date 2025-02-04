# https://school.programmers.co.kr/learn/courses/30/lessons/49993
# Summer/Winter Coding(~2018)

import re

def solution(skill, skill_trees):
    answer = 0
    pattern = f'[{skill}]'
    for data in skill_trees:
        result = re.findall(pattern, data)
        s_idx = 0
        for r in result:
            if r != skill[s_idx]:
                break
            s_idx += 1
        else:
            answer += 1
            
    return answer