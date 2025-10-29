// https://school.programmers.co.kr/learn/courses/30/lessons/181858
// 코딩 기초 트레이닝: 무작위로 K개의 수 뽑기

import Foundation

func solution(_ arr:[Int], _ k:Int) -> [Int] {
    var answer: [Int] = []
    var data: Set<Int> = []
    for num in arr {
        if answer.count == k {
            break
        }
        if !data.contains(num) {
            answer.append(num)
            data.insert(num)
        }
    }
    if answer.count != k {
        answer.append(contentsOf: Array(repeating: -1, count: k - answer.count))
    }
    return answer
}