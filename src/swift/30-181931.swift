// https://school.programmers.co.kr/learn/courses/30/lessons/181931
// 코딩 기초 트레이닝

import Foundation

func solution(_ a:Int, _ d:Int, _ included:[Bool]) -> Int {
    var answer: Int = 0
    for (i, bool) in included.enumerated() {
        if bool {
            answer += a + d * i
        }
    }
    return answer
}