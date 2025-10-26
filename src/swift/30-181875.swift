// https://school.programmers.co.kr/learn/courses/30/lessons/181875
// 코딩 기초 트레이닝: 배열에서 문자열 대소문자 변환하기

import Foundation

func solution(_ strArr:[String]) -> [String] {
    var answer: [String] = strArr
    for i in 0..<strArr.count {
        if i % 2 == 0 {
            answer[i] = answer[i].lowercased()
        }
        else {
            answer[i] = answer[i].uppercased()
        }
    }
    return answer
}