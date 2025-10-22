// https://school.programmers.co.kr/learn/courses/30/lessons/181897
// 코딩 기초 트레이닝: 리스트 자르기

import Foundation

func solution(_ n:Int, _ slicer:[Int], _ num_list:[Int]) -> [Int] {
    let a: Int = slicer[0]
    let b: Int = slicer[1]
    let c: Int = slicer[2]
    switch n {
        case 1:
            return Array(num_list[...b])
        case 2:
            return Array(num_list[a...])
        case 3:
            return Array(num_list[a...b])
        default:
            var answer: [Int] = []
            for i in stride(from: a, through: b, by: c) {
                answer.append(num_list[i])
            }
            return answer
    }
    return []
}