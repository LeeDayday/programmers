// https://school.programmers.co.kr/learn/courses/30/lessons/181867
// 코딩 기초 트레이닝: x 사이의 개수

import Foundation

func solution(_ myString:String) -> [Int] {
    var answer: [Int] = []
    var count: Int = 0
    for ch in myString {
        if ch == "x" {
            answer.append(count)
            count = 0
        }
        else {
            count += 1
        }
    }
    
    answer.append(count)
    return answer
}