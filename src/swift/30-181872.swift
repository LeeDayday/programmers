// https://school.programmers.co.kr/learn/courses/30/lessons/181872
// 코딩 기초 트레이닝: 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기

import Foundation

func solution(_ myString:String, _ pat:String) -> String {
    if let range = myString.range(of: pat, options: .backwards) {
        return String(myString[..<range.upperBound])
    }
    return ""
}