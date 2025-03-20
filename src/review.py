# 복습 - 숫자 변환하기
# https://school.programmers.co.kr/learn/courses/30/lessons/154538

# O(N)

from collections import deque
def solution(x, y, n):
    queue = deque([(x, 0)])
    visited = {x}
    while queue:
        num, cnt = queue.popleft()
        if num == y:
            return cnt
        if num + n not in visited and num + n <= y:
            visited.add(num + n)
            queue.append((num + n, cnt + 1))
        if num * 2 not in visited and num * 2 <= y:
            visited.add(num * 2)
            queue.append((num * 2, cnt + 1))
        if num * 3 not in visited and num * 3 <= y:
            visited.add(num * 3)
            queue.append((num * 3, cnt + 1))
        
    return -1