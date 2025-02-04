# https://school.programmers.co.kr/learn/courses/30/lessons/49993
# Summer/Winter Coding(~2018)

def solution(skill, skill_trees):
    answer = 0    
    skill_set = set(skill)
    
    for data in skill_trees:
        s_idx = 0
        for i in range(len(data)):
            # 스킬트리 순서 만족
            if s_idx < len(skill) and data[i] == skill[s_idx]:
                s_idx += 1
            else:
                # 스킬트리 순서 위배
                if data[i] in skill_set:
                    break
        else:
            answer += 1
                    
    return answer