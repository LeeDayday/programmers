// https://school.programmers.co.kr/learn/courses/30/lessons/181862
// 코딩 기초 트레이닝: 세 개의 구분자

import Foundation

func solution(_ myStr:String) -> [String] {
    let answer = Array(myStr.split(whereSeparator: { $0 == "a" || $0 == "b" || $0 == "c" }).map { String($0) })
    if answer == [] {
        return ["EMPTY"]
    }
    return answer
}