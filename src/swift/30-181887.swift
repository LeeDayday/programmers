// https://school.programmers.co.kr/learn/courses/30/lessons/181887
// 코딩 기초 트레이닝: 홀수 vs 짝수

import Foundation

func solution(_ num_list:[Int]) -> Int {
    var result1: Int = 0
    var result2: Int = 0
    for (i, num) in num_list.enumerated() {
        if i % 2 == 0 {
            result1 += num
        }
        else {
            result2 += num
        }
    }
    return max(result1, result2)
}