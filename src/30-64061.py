# https://school.programmers.co.kr/learn/courses/30/lessons/64061
# 2019 카카오 개발자 겨울 인턴십

# col_idx의 가장 꼭대기 인형 위치를 반환하는 함수
# 꼭대기 인형 row 반환, 없으면 -1
def last_doll(board, col_idx):
    # 바닥 층에 인형이 없는 경우, 해당 열은 비어있음
    if board[-1][col_idx] == 0:
        return -1
    else:
        idx = len(board) - 1
        while idx >= 0 and board[idx][col_idx] != 0:
            idx -= 1
        return idx + 1
    

def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        #print(f"move: {move}")
    
        # move 번째 열에 인형이 있는지 확인
        doll_row = last_doll(board, move-1)
        #print(f"doll_row: {doll_row}")
        if doll_row == -1:
            continue
        
        # 인형 뽑기
        
        doll = board[doll_row][move-1]
        #print(f"doll: {doll}")
        board[doll_row][move-1] = 0
        # 바구니가 비어있다면 인형 바로 넣기
        if len(stack) == 0:
            #print("바구니 empty")
            stack.append(doll)
        # 바구니가 차 있다면, 바구니의 top과 비교하기
        else:
            tmp_top = stack.pop() # top 임의로 pop
            #print(f"{tmp_top}와 {doll} 비교")
            # 인형이 동일하다면 answer 증가, 바구니에 넣지 않기
            if doll == tmp_top:
                answer += 2
            # 동일하지 않다면 바구니에 넣기
            else:
                stack.append(tmp_top) # top 다시 넣기
                stack.append(doll)
        
    return answer