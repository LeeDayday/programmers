// https://school.programmers.co.kr/learn/courses/30/lessons/181929
// 코딩 기초 트레이닝

import Foundation

func solution(_ num_list:[Int]) -> Int {
    var result1: Int = 1
    var result2: Int = 0
    for num in num_list {
        result1 *= num
        result2 += num
    }
    if result1 < result2 * result2 {
        return 1
    }
    
    return 0
}