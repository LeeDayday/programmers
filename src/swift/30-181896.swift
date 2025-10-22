// https://school.programmers.co.kr/learn/courses/30/lessons/181896
// 코딩 기초 트레이닝: 첫 번째로 나오는 음수

import Foundation

func solution(_ num_list:[Int]) -> Int {
    for i in 0..<num_list.count {
        if num_list[i] < 0 {
            return i
        }
    }
    return -1
}