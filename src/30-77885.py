# https://school.programmers.co.kr/learn/courses/30/lessons/77885
# 연습문제

def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2:
            binary = bin(number)[2:]  # 2진수 변환 ('0b' 제거)
            if '0' in binary:
                # 1. 가장 오른쪽의 '0'을 '1'로 바꾸고, 그 뒤의 '1'을 '0'으로 변경
                index = binary.rfind('0')  # 가장 오른쪽 '0' 찾기
                new_binary = binary[:index] + '10' + binary[index+2:]
            else:
                # 2. '0'이 없는 경우 (예: 7 -> '111' -> '1011')
                new_binary = '10' + binary[1:]  # 맨 앞에 '10' 추가
            answer.append(int(new_binary, 2))  # 10진수 변환 후 추가
            
        # 짝수의 경우, 최하위 비트가 항상 0
        # 따라서 f(x) = x + 1 만족
        else:
            answer.append(number + 1)
    return answer