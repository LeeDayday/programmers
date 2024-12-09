# https://school.programmers.co.kr/learn/courses/30/lessons/12953
# N개의 최소공배수
from math import gcd

def solution(arr):
    def lcm(a, b):
        return a * b // gcd(a, b)
    
    answer = arr[0]
    for num in arr[1:]:
        answer = lcm(answer, num)
    
    return answer