# https://school.programmers.co.kr/learn/courses/30/lessons/12980
# Summer/Winter Coding(~2018)

def solution(n):
    ans = 0
    # 최대한 순간 이동
    while n > 0:
        if n % 2 == 0: 
            n = n // 2
        else: 
            n = n - 1
            ans += 1
    
    return ans