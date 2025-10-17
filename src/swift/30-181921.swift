// https://school.programmers.co.kr/learn/courses/30/lessons/181921
// 코딩 기초 트레이닝: 배열 만들기 2

import Foundation

func solution(_ l:Int, _ r:Int) -> [Int] {
    var queue: [Int] = [5]
    var answer: [Int] = []
    while !queue.isEmpty {
        guard let num = queue.popLast() else { break }
        if num > r {
            continue
        }
        if l <= num {
            answer.append(num)
        }
        if num * 10 <= r {
            queue.append(num * 10)
        }
        if num * 10 + 5 <= r {
            queue.append(num * 10 + 5)
        }

    }
    return answer.isEmpty ? [-1] : answer.sorted()
}