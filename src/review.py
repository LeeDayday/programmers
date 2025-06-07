# 복습 - 영어 끝말잇기
# https://school.programmers.co.kr/learn/courses/30/lessons/12981

# O(N)

from collections import defaultdict
def solution(n, words):
    result = defaultdict(list)
    memory = set()
    for idx, word in enumerate(words):
        # 이미 사용한 단어를 또 사용한 경우
        if word in memory:
            break
        # 끝말잇기가 이어지지 않은 경우
        if idx != 0:
            if result[(idx - 1) % n][-1][-1] != word[0]:
                break
        memory.add(word)
        result[idx % n].append(word)
    else:
         return [0, 0]
        
    return [idx % n + 1, len(result[idx % n]) + 1]


