// https://school.programmers.co.kr/learn/courses/30/lessons/181900
// 코딩 기초 트레이닝: 글자 지우기

import Foundation

func solution(_ my_string: String, _ indices: [Int]) -> String {
    let toRemove = Set(indices)
    var answer = ""
    answer.reserveCapacity(my_string.count - toRemove.count)

    for (i, ch) in my_string.enumerated() {
        if !toRemove.contains(i) { 
            answer.append(ch) 
        }
    }
    return answer
}
