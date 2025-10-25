// https://school.programmers.co.kr/learn/courses/30/lessons/181882
// 코딩 기초 트레이닝: 조건에 맞게 수열 변환하기 1

import Foundation

func solution(_ arr:[Int]) -> [Int] {
    var answer: [Int] = arr
    for (i, num) in answer.enumerated() {
        if num >= 50 && num % 2 == 0 {
            answer[i] = num / 2
        }
        else if num < 50 && num % 2 == 1 {
            answer[i] = num * 2
        }
    }
    return answer
}