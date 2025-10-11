# https://school.programmers.co.kr/learn/courses/30/lessons/42895
# 동적계획법

def solution(N, number):
    if N == number:
        return 1
    data = [{int(str(N) * i)} for i in range(1, 9)] # data[i]: N을 (i+1) 개 사용하여 만들 수 있는 값의 집합
    

    for i in range(8):
        for j in range(i):
            for num1 in data[j]: # num1: N을 (j + 1)개를 사용하여 만들 수 있는 값
                for num2 in data[i - j - 1]: # num2: N을 
                    data[i].add(num1 + num2)
                    data[i].add(num1 - num2)
                    data[i].add(num1 * num2)
                    if num2 != 0:
                        data[i].add(num1 // num2)
                    if number in data[i]:
                        return i + 1
    return -1
                    
            