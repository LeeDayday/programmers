// https://school.programmers.co.kr/learn/courses/30/lessons/181923
// 코딩 기초 트레이닝: 수열과 구간 쿼리 2

import Foundation

func solution(_ arr:[Int], _ queries:[[Int]]) -> [Int] {
    var answer: [Int] = []
    
    for query in queries {
        var tmp: Int = query[2]
        var flag: Bool = false
        for i in query[0]...query[1] {
            if arr[i] > query[2] {
                if flag {
                    tmp = min(tmp, arr[i])
                }
                else {
                    tmp = arr[i]
                    flag = true
                }
            }
        }
        if tmp == query[2] {
            answer.append(-1)
        }
        else {
            answer.append(tmp)
        }
    }
    return answer
}