// https://school.programmers.co.kr/learn/courses/30/lessons/181886
// 코딩 기초 트레이닝: 5명씩

import Foundation

func solution(_ names:[String]) -> [String] {
    var answer: [String] = []
    for i in stride(from: 0, to: names.count, by: 5) {
        answer.append(names[i])
    }
    return answer
}