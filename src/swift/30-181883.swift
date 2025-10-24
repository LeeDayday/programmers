// https://school.programmers.co.kr/learn/courses/30/lessons/181883
// 코딩 기초 트레이닝: 수열과 구간 쿼리 1

import Foundation

func solution(_ arr:[Int], _ queries:[[Int]]) -> [Int] {
    var answer: [Int] = arr
    for query in queries {
        let s: Int = query[0]
        let e: Int = query[1]
        for i in s...e {
            answer[i] += 1
        }
    }
    return answer
}