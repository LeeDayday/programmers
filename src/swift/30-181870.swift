// https://school.programmers.co.kr/learn/courses/30/lessons/181870
// 코딩 기초 트레이닝: ad 제거하기

import Foundation

func solution(_ strArr:[String]) -> [String] {
    var answer: [String] = []
    for str in strArr {
        if !str.contains("ad") {
            answer.append(str)
        }
    }
    return answer
}