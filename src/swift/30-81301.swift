// https://school.programmers.co.kr/learn/courses/30/lessons/81301
// 2021 카카오 채용연계형 인턴십: 숫자 문자열과 영단어

import Foundation

func solution(_ s:String) -> Int {
    var answer: String = ""
    var tmp: String = ""
    let data: [String: String] = [
        "zero": "0", "one": "1", "two": "2",
        "three": "3", "four": "4", "five": "5", 
        "six": "6", "seven": "7", "eight": "8", "nine": "9"
    ]
    
    for ch in s {
        if ch.isNumber {
            answer.append(ch)
            continue
        }
        tmp.append(ch)
        if let digit = data[tmp] {
            answer.append(digit)
            tmp.removeAll()
        }
    }
    
    return Int(answer)!
}