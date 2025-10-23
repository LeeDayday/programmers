// https://school.programmers.co.kr/learn/courses/30/lessons/181892
// 코딩 기초 트레이닝: n 번째 원소부터

import Foundation

func solution(_ num_list:[Int], _ n:Int) -> [Int] {
    let index:Int = n - 1
    return Array(num_list[index...])
}