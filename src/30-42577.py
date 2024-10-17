# https://school.programmers.co.kr/learn/courses/30/lessons/42577
# 해시

def solution(phone_book):
    phone_book.sort() # 사전 순으로 정렬

    for i in range(len(phone_book) - 1):
        tmp = phone_book[i + 1]
        if phone_book[i] == tmp[:len(phone_book[i])]:
            return False
    return True