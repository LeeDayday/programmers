# https://school.programmers.co.kr/learn/courses/30/lessons/42579
# 해시

from collections import Counter, defaultdict

def solution(genres, plays):
    answer = []
    count = Counter()
    
    data = defaultdict(list)
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        count[genre] += play
        data[genre].append((play, i)) # 재생 수, 고유 번호
        
    # 많이 재생된 장르 내림차순 정렬
    count = count.most_common() # (장르, 재생 수)
    
    # 장르 별 (재생 수 기준 내림차순), (고유 번호 오름차순) 정렬
    for i in range(len(count)):
        data[count[i][0]].sort(key=lambda x: (-x[0], x[1]))
    
    for genre, _ in count:
        if len(data[genre]) == 1:
            answer.append(data[genre][0][1])
        else:
            for i in range(2):
                answer.append(data[genre][i][1])
    return answer