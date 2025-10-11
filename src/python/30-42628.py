# https://school.programmers.co.kr/learn/courses/30/lessons/42584
# 힙(Heap)

from heapq import heappush, heappop
from collections import defaultdict

def solution(operations):
    minheap = []
    maxheap = []
    entry_count = defaultdict(int) # 유효한 요소인지 검사 (minheap, maxheap 중복 삭제 및 삭제된 요소 접근 제한)
    
    for operation in operations:
        cmd, num = operation.split()
        num = int(num)
        
        if cmd == 'I':
            heappush(minheap, num)
            heappush(maxheap, -num)
            entry_count[num] += 1
            
        elif cmd == 'D':
            # 최댓값 삭제
            if num == 1:
                # 이미 삭제된 요소가 있는 경우, 삭제 (maxheap 업데이트)
                while maxheap and entry_count[-maxheap[0]] == 0:
                    heappop(maxheap)
                if maxheap:
                    entry_count[-heappop(maxheap)] -= 1
            # 최솟값 삭제
            else: 
                # minheap 업데이트
                while minheap and entry_count[minheap[0]] == 0:
                    heappop(minheap)
                if minheap:
                    entry_count[heappop(minheap)] -= 1
        
        # minheap, maxheap 업데이트
        while maxheap and entry_count[-maxheap[0]] == 0:
                    heappop(maxheap)
        while minheap and entry_count[minheap[0]] == 0:
                    heappop(minheap)        
        
        if len(minheap) > 1:
            answer = [-maxheap[0], minheap[0]]
        else:
            answer = [0, 0]
    return answer