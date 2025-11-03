// https://school.programmers.co.kr/learn/courses/30/lessons/181836
// 코딩 기초 트레이닝: 그림 확대

import Foundation

func solution(_ picture:[String], _ k:Int) -> [String] {
    var answer: [String] = []
    for row in picture {
        var result = ""
        for ch in row {
            for _ in 0..<k {
                result += String(ch)
            }
        }
        for _ in 0..<k {
            answer.append(result)
        }
    }
    return answer
}