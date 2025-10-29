// https://school.programmers.co.kr/learn/courses/30/lessons/181861
// 코딩 기초 트레이닝: 배열의 원소만큼 추가하기

import Foundation

func solution(_ arr:[Int]) -> [Int] {
    var answer: [Int] = []
    for num in arr {
        for _ in 0..<num {
            answer.append(num)
        }
    }
    return answer
}