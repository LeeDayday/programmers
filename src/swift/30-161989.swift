// https://school.programmers.co.kr/learn/courses/30/lessons/161989
// 연습문제: 덧칠하기

import Foundation

func solution(_ n:Int, _ m:Int, _ section:[Int]) -> Int {
    let k: Int = section.count
    var idx: Int = 0
    var answer: Int = 0
    while idx < k {
        let start: Int = section[idx]
        while idx < k && start + m > section[idx] {
            idx += 1
        }
        answer += 1
    }
    return answer
}