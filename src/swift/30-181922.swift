// https://school.programmers.co.kr/learn/courses/30/lessons/181922
// 코딩 기초 트레이닝: 수열과 구간 쿼리 4

import Foundation

func solution(_ arr:[Int], _ queries:[[Int]]) -> [Int] {
    var answer: [Int] = arr
    for query in queries {
        print(query)
        for i in query[0]...query[1] {
            guard i >= 0 && i < arr.count else {continue}
            if i % query[2] == 0 {
                answer[i] += 1
            }
        }
    }
    return answer
}