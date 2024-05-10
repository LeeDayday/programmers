# https://school.programmers.co.kr/learn/courses/30/lessons/64061
# 2019 카카오 개발자 겨울 인턴십


def solution(board, moves):
    answer = 0
    stack = []

    for i in moves:
        for j in range(len(board)):
            # 해당 column에 인형이 존재한다면 인형 뽑기 수행
            if board[j][i-1] != 0:
                # 인형 뽑기
                stack.append(board[j][i-1])
                # 보드에 인형 제거하기
                board[j][i-1] = 0

                # stack에 인형이 있는 경우, 꼭대기 인형과 비교
                if len(stack) > 1:
                    if stack[-1] == stack[-2]:
                        stack.pop()
                        stack.pop()
                        answer += 2
                break

        
    return answer