// https://school.programmers.co.kr/learn/courses/30/lessons/181879
// 코딩 기초 트레이닝: 길이에 따른 연산

import Foundation

func solution(_ num_list:[Int]) -> Int {
    if num_list.count >= 11 {
        return num_list.reduce(0, +)
    }
    return num_list.reduce(1, *)
}