// https://school.programmers.co.kr/learn/courses/30/lessons/142086
// 연습문제: 가장 가까운 같은 글자

import Foundation

import Foundation

func solution(_ s:String) -> [Int] {
    var answer: [Int] = []
    var data = [Character: Int]() // 알파벳 별 마지막 index 값 저장

    for (i, ch) in s.enumerated() {
        if let prev = data[ch] {
            answer.append(i - prev)
        } else {
            answer.append(-1)
        }
        data[ch] = i
    }
    
    return answer
}