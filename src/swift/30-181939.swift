// https://school.programmers.co.kr/learn/courses/30/lessons/181939
// 코딩 기초 트레이닝

import Foundation

func solution(_ a:Int, _ b:Int) -> Int {
    let ab: Int = Int("\(a)\(b)")!
    let ba: Int = Int("\(b)\(a)")!
    return max(ab, ba)
}