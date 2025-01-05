# https://school.programmers.co.kr/learn/courses/30/lessons/17677
# 2018 KAKAO BLIND RECRUITMENT

from collections import Counter

def get_pair(data):
    # 영문자로 된 글자쌍만 유효
    if ('A' <= data[0].upper() <= 'Z') and ('A' <= data[1].upper() <= 'Z'):
        return data.upper()
    return False
            
def solution(str1, str2):
    answer = 0
    pair_1 = Counter()
    pair_2 = Counter()
    
    for i in range(len(str1) - 1):
        pair = get_pair(str1[i:i+2])
        if pair:
            pair_1[pair] += 1
    
    for i in range(len(str2) - 1):
        pair = get_pair(str2[i:i+2])
        if pair:
            pair_2[pair] += 1

    # 유사도: y/x (단, x != 0)
    y = sum((pair_1 & pair_2).values())
    x = sum((pair_1 | pair_2).values())
    
    if x == 0:
        if x == y:
            answer = 65536
    else:
        answer = int((y / x) * 65536)
    return answer

