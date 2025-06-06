# 복습 - 마법의 엘리베이터
# https://school.programmers.co.kr/learn/courses/30/lessons/148653

# O(N)

def solution(storey):
    answer = 0
    
    while storey:
        r = storey % 10
        if r > 5:
            storey += 10
            answer += 10 - r
        elif r < 5:
            answer += r
        # 5 인 경우, 다음 자리 수까지 고려
        else:
            if ((storey // 10) % 10) > 4:
                storey += 10
            answer += r
        storey //= 10
            
    return answer