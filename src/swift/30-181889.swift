// https://school.programmers.co.kr/learn/courses/30/lessons/181889
// 코딩 기초 트레이닝: n 번째 원소까지

import Foundation

func solution(_ num_list:[Int], _ n:Int) -> [Int] {
    return Array(num_list[..<n])
}