// https://school.programmers.co.kr/learn/courses/30/lessons/181855
// 코딩 기초 트레이닝: 문자열 묶기

import Foundation

func solution(_ strArr:[String]) -> Int {
    let data = Dictionary(grouping: strArr, by: { $0.count })
    var answer: Int = 0
    for (k, v) in data {
        answer = max(answer, v.count)
    }
    return answer
}