// https://school.programmers.co.kr/learn/courses/30/lessons/181924
// 코딩 기초 트레이닝: 수열과 구간 쿼리 3

import Foundation

func solution(_ arr:[Int], _ queries:[[Int]]) -> [Int] {
    var answer: [Int] = arr

    for query in queries {
        let i = query[0]
        let j = query[1]
        answer.swapAt(i, j)
    }
    return answer
}