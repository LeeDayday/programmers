// https://school.programmers.co.kr/learn/courses/30/lessons/181928
// 코딩 기초 트레이닝

import Foundation

func solution(_ num_list:[Int]) -> Int {
    var odd: Int = 0
    var even: Int = 0
    
    for num in num_list {
        if num % 2 == 1 {
            odd *= 10
            odd += num
        }
        else {
            even *= 10
            even += num
        }
    }
    return odd + even
}