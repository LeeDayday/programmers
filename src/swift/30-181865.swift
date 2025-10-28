// https://school.programmers.co.kr/learn/courses/30/lessons/181865
// 코딩 기초 트레이닝: 간단한 식 계산하기

import Foundation

func solution(_ binomial:String) -> Int {
    var data = binomial.split(separator: " ").map { String($0) }
    switch data[1] {
        case "+":
            return Int(data[0])! + Int(data[2])!
        case "-":
            return Int(data[0])! - Int(data[2])!
        default:
            return Int(data[0])! * Int(data[2])!
    }

}