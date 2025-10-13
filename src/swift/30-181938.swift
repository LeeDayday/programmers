// https://school.programmers.co.kr/learn/courses/30/lessons/181938
// 코딩 기초 트레이닝

import Foundation

func solution(_ a:Int, _ b:Int) -> Int {
    let result: Int = Int("\(a)\(b)")!
    return max(result, 2 * a * b)
}