// https://school.programmers.co.kr/learn/courses/30/lessons/176963
// 연습문제: 추억 점수

import Foundation

func solution(_ name:[String], _ yearning:[Int], _ photo:[[String]]) -> [Int] {
    let data: [String: Int] = Dictionary(uniqueKeysWithValues: 
        zip(name, yearning)
    )
    var answer: [Int] = []
    
    for row in photo {
        var total: Int = 0
        for name in row {
            if data[name] != nil {
                total += data[name]!
            }
        }
        answer.append(total)
    }
    
    return answer
}   