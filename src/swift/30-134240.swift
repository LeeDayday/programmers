// https://school.programmers.co.kr/learn/courses/30/lessons/134240
// 연습문제: 푸드 파이트 대회

import Foundation

func solution(_ food:[Int]) -> String {
    var answer: String = ""
    for i in 1..<food.count {
        if food[i] / 2 > 0 {
            answer += String(repeating: String(i), count: food[i]/2)
        }
    }
    return answer + "0" + String(answer.reversed())
}