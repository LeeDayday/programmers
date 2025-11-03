// https://school.programmers.co.kr/learn/courses/30/lessons/181835
// 코딩 기초 트레이닝: 조건에 맞게 수열 변환하기 3

import Foundation

func solution(_ arr:[Int], _ k:Int) -> [Int] {
    return k % 2 == 1 ? arr.map { $0 * k } : arr.map { $0 + k }
}