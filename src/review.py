# 복습 - 전화번호 목록
# https://school.programmers.co.kr/learn/courses/30/lessons/42577

# O(NlogN)

def solution(phone_book):
    phone_book.sort() # 문자열 사전순 정렬
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False
    return True