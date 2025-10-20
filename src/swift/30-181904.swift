// https://school.programmers.co.kr/learn/courses/30/lessons/181904
// 코딩 기초 트레이닝: 세로 읽기

import Foundation

func solution(_ my_string:String, _ m:Int, _ c:Int) -> String {
    var answer: String = ""
    let startIndex = my_string.startIndex
    for i in stride(from: 0, to: my_string.count, by: m) {
        let index = my_string.index(startIndex, offsetBy: i + c - 1)
        answer.append(my_string[index])
    }
    return answer
}