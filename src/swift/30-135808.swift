// https://school.programmers.co.kr/learn/courses/30/lessons/135808
// 연습문제: 과일 장수

import Foundation

func solution(_ k:Int, _ m:Int, _ score:[Int]) -> Int {
    let sortedScore: [Int] = score.sorted(by: >)
    var answer: Int = 0
    for idx in stride(from: m - 1, to: score.count, by: m){
        answer += sortedScore[idx] * m
    }
    return answer
}