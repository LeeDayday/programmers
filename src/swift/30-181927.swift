// https://school.programmers.co.kr/learn/courses/30/lessons/181927
// 코딩 기초 트레이닝: 마지막 두 원소

import Foundation

func solution(_ num_list:[Int]) -> [Int] {
    var answer: Array = num_list
    var n: Int = num_list.count
    if num_list[n - 1] > num_list[n - 2] {
        answer.append(num_list[n - 1] - num_list[n - 2])
    }
    else {
        answer.append(num_list[n - 1] * 2)
    }
    return answer
}