# https://school.programmers.co.kr/learn/courses/30/lessons/178870
# 연습문제제

def solution(sequence, k):
    start, end = 0, 0
    answer = [0, len(sequence)]
    
    cnt = 0
    while end < len(sequence):
        cnt += sequence[end]
        # start를 늘리며 부분 수열 합이 k 를 만족하는 경우 계산
        while cnt >= k and start <= end:
            if cnt == k:
                # 부분 수열 합이 k를 만족하는 경우, 길이가 짧은 수열 저장
                if end - start < answer[1] - answer[0]:
                    answer[0] = start
                    answer[1] = end
            cnt -= sequence[start]
            start += 1
        end += 1

    return answer
        