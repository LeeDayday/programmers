# https://school.programmers.co.kr/learn/courses/30/lessons/148653
# 연습문제

def solution(storey):
    answer = 0
    
    while storey != 0:
        last_number = storey % 10
        if last_number < 5:
            answer += last_number
        elif last_number > 5:
            storey += 10
            answer += 10 - last_number
        else: # 마지막 자리 수가 5인 경우, 다음 자리 수까지 고려해야 함 (올리는 것이 나은지, 내리는 것이 나은지)
            if ((storey // 10) % 10) > 4:
                storey += 10
            answer += last_number
                
            
        storey //= 10
        
    return answer