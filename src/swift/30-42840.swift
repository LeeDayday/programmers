// https://school.programmers.co.kr/learn/courses/30/lessons/42840
// 완전탐색: 모의고사

import Foundation

func solution(_ answers:[Int]) -> [Int] {
    let data: [[Int]] = [
        [1, 2, 3, 4, 5], 
        [2, 1, 2, 3, 2, 4, 2, 5], 
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    var scores = Array(repeating: 0, count: 3)
    
    for (i, ans) in answers.enumerated() {
        for p in 0..<3 {
            if data[p][i % data[p].count] == ans {
                scores[p] += 1
            }
        }
    }
    
    let maxScore = scores.max()!
    
    return scores.enumerated()
        .filter { $0.element == maxScore }
        .map { $0.offset + 1 }
}