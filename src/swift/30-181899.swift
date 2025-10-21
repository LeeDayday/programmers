// https://school.programmers.co.kr/learn/courses/30/lessons/181899
// 코딩 기초 트레이닝: 카운트 다운

import Foundation

func solution(_ start_num:Int, _ end_num:Int) -> [Int] {
    return Array(stride(from: start_num, through: end_num, by: -1))
}