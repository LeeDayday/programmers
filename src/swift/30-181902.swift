// https://school.programmers.co.kr/learn/courses/30/lessons/181902
// 코딩 기초 트레이닝: 문자 개수 세기

import Foundation

func solution(_ my_string:String) -> [Int] {
    var answer: [Int] = Array(repeating: 0, count: 52)
    let asciiA = "A".first!.asciiValue!
    let asciia = "a".first!.asciiValue!
    for ch in my_string {
        print(ch)
        if ch.isUppercase {
            answer[Int(ch.asciiValue! - asciiA)] += 1
        }
        else {
            answer[Int(ch.asciiValue! - asciia) + 26] += 1
        }
    }
    return answer
}