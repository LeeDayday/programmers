# https://school.programmers.co.kr/learn/courses/30/lessons/70129
# 월간 코드 챌린지 시즌 1

def dec_to_bin(n: int) -> str:
    result = ''
    
    while n:
        result += str(n % 2)
        n = n // 2
        
    return result[::-1]
        
    
def solution(s):
    answer = [0, 0] # 이진변환 횟수, 제거한 0의 개수
    while True:
        cnt = 0 # 0의 개수
        # 문자열 내 0의 개수 계산
        for ch in s:
            if ch == '0':
                cnt += 1
        # 문자열이 '1' 인 경우, 종료
        if len(s) == 1 and cnt == 0:
            break
            
        # 이진 변환 수행
        answer[0] += 1
        answer[1] += cnt
        s = dec_to_bin(len(s) - cnt)
                
    return answer