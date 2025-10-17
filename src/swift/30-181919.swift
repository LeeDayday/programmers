// https://school.programmers.co.kr/learn/courses/30/lessons/181919
// 코딩 기초 트레이닝: 콜라츠 수열 만들기

import Foundation

func solution(_ n:Int) -> [Int] {
    var answer: [Int] = [n]
    var num: Int = n
    while num != 1 {
        if num % 2 == 0 {
            num /= 2
            answer.append(num)
        }
        else {
            num = 3 * num + 1
            answer.append(num)
        }
    }
    return answer
}