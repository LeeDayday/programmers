// https://school.programmers.co.kr/learn/courses/30/lessons/181909
// 코딩 기초 트레이닝: 접미사 배열

import Foundation

func solution(_ my_string:String) -> [String] {
    var answer: [String] = []    
    for i in 0..<my_string.count {
        let start = my_string.index(my_string.startIndex, offsetBy: i)
        answer.append(String(my_string[start...]))
    }
    return answer.sorted()
}