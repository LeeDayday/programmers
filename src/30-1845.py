# https://school.programmers.co.kr/learn/courses/30/lessons/1845
# 해시


from itertools import combinations


def solution(nums):
    answer = 0
    N = len(nums)
    nums = set(nums)
    if N // 2 <= len(nums):
        answer = N // 2
    else:
        answer = len(nums)
          
    return answer