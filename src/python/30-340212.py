# https://school.programmers.co.kr/learn/courses/30/lessons/340212
# PCCP 기출문제

def solution(diffs, times, limit):
    answer = []
    start = 1
    end = max(diffs)
    n = len(diffs)
    
    def puzzle(level, time):
        for i in range(n):
            if level >= diffs[i]:
                time -= times[i]
            else:
                time -= (times[i] + times[i - 1]) * (diffs[i] - level) + times[i]
        if time < 0:
            return False
        return True
                
    while start <= end:
        mid = (start + end) // 2
        if puzzle(mid, limit):
            end = mid - 1
        else:
            start = mid + 1
            
    return start