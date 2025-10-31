// https://school.programmers.co.kr/learn/courses/30/lessons/181852
// 코딩 기초 트레이닝: 뒤에서 5등 위로

import Foundation

func solution(_ num_list:[Int]) -> [Int] {
    return Array(num_list.sorted()[5...])
}
