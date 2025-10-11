# https://school.programmers.co.kr/learn/courses/30/lessons/17680
# 2018 KAKAO BLIND RECRUITMENT

def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    for city in cities:
        city = city.lower()
        if cacheSize:
            # cache miss
            if not city in cache:
                if len(cache) == cacheSize:
                    # LRU 수행
                    cache.pop(0)
                cache.append(city)
                answer += 5

            else:
                cache.pop(cache.index(city)) # 기존 도시 삭제
                cache.append(city) # 새로 다시 추가
                answer += 1
        else:
            answer += 5 # cacheSize가 0인 경우 무조건 cache miss
            
    return answer
