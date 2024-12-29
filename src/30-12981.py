# https://school.programmers.co.kr/learn/courses/30/lessons/12981
# Summer/Winter Coding(~2018)

from collections import defaultdict

def solution(n, words):
    data = defaultdict(list)

    def check_condition(i, words):
        # 앞사람이 말한 단어의 마지막 문자로 시작하지 않는 경우
        if i > 0 and words[i - 1][-1] != words[i][0]:
            return True
        # 이전에 말한 단어를 말하는 경우
        if words[i] in data[words[i][0]]:
            return True
        # 한 글자 단어를 말하는 경우
        if len(words[i]) == 0:
            return True
        return False

    for i in range(len(words)):
        if check_condition(i, words):
            return [i % n + 1, i // n + 1]
        else:
            data[words[i][0]].append(words[i])
    else:
        return [0, 0]        
