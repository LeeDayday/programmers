// https://school.programmers.co.kr/learn/courses/30/lessons/138477
// 연습문제: 명예의 전당(1)

import Foundation

func solution(_ k:Int, _ score:[Int]) -> [Int] {
    var answer: [Int] = []
    var topK: [Int] = []
    
    for i in 0..<score.count {
        topK.append(score[i])
        topK.sort(by:>)
        if topK.count > k {
            topK.removeLast()
        }
        answer.append(topK.last!)
    }
    return answer
}