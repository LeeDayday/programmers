# https://school.programmers.co.kr/learn/courses/30/lessons/42890
# 2019 카카오 블라인드 채용


from itertools import combinations

def solution(relation):
    answer = 0
    result = []
        
    cols = list(map(list, zip(*relation)))
    col_cnt = len(cols)
    col_idx = [i for i in range(col_cnt)]

    total_cnt = len(relation)
    # 가능한 모든 column 조합
    for i in range(1, col_cnt+1): 
        combs = combinations(col_idx, i)
        for comb_idx in combs:
            tmp_col = set(zip(*[cols[c] for c in comb_idx])) # 조합에 해당하는 col 내용만
            # 유일성 검증
            if len(tmp_col) == total_cnt:
                # 최소성 검증
                for r in result:
                    print(r)
                    if set(r).issubset(comb_idx): # comb_idx이 이미 존재한다면 최소성 만족 X
                        break
                else:
                    result.append(comb_idx)         
            else:
                continue
    answer = len(result)
    return answer