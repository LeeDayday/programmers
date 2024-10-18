# https://school.programmers.co.kr/learn/courses/30/lessons/42578
# 해시

def solution(clothes):
    answer = 1
    c_type = ['headgear', 'eyewear', 'face']
    clothes_dict = {}
    
    for c_name, c_type in clothes:
        if c_type not in clothes_dict:
            clothes_dict[c_type] = [c_name]
        else:
            clothes_dict[c_type].append(c_name)
            
    cnt = [0] * (len(clothes_dict)) # 의상 종류 당 의상 이름의 수
    i = 0
    for c_name_list in clothes_dict.values():
        cnt[i] += len(c_name_list)
        i += 1
    
    # 종류가 한 가지인 경우
    if len(cnt) == 1:
        answer = cnt[0]
    else:
        for i in range(len(cnt)):
            answer = answer * (cnt[i] + 1)
        answer -= 1 # 모든 종류의 의상을 입지 않는 경우 제외
    return answer