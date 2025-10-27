// https://school.programmers.co.kr/learn/courses/30/lessons/181869
// 코딩 기초 트레이닝: 공백으로 구분하기 1

import Foundation

func solution(_ my_string:String) -> [String] {
    var answer: [String] = []
    for str in my_string.split(separator: " ") {
        answer.append(String(str))
    }
    return answer
}