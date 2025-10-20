// https://school.programmers.co.kr/learn/courses/30/lessons/181903
// 코딩 기초 트레이닝: qr code

import Foundation

func solution(_ q:Int, _ r:Int, _ code:String) -> String {
    var answer: String = ""
    let startIndex = code.startIndex
    for i in 0..<code.count {
        if i % q == r {
            answer.append(code[code.index(startIndex, offsetBy: i)])
        }
    }
    return answer
}