# https://school.programmers.co.kr/learn/courses/30/lessons/42576
# 해시

def solution(participant, completion):
    answer = ''
    participant_dict = {} # 참가 선수 명단
    
    for name in participant:
        participant_dict[name] = participant_dict.get(name, 0) + 1
        
    for name in completion:
        participant_dict[name] -= 1

    for name, cnt in participant_dict.items():
        if cnt == 1:
            answer = name
            break
            
    return answer