// https://school.programmers.co.kr/learn/courses/30/lessons/181884
// 코딩 기초 트레이닝: n보다 커질 때까지 더하기

import Foundation

func solution(_ numbers:[Int], _ n:Int) -> Int {
    var result: Int = 0
    for i in 0..<numbers.count {
        if result > n {
            break
        }
        result += numbers[i]
    }
    return result
}