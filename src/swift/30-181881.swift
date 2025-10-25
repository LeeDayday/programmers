// https://school.programmers.co.kr/learn/courses/30/lessons/181881
// 코딩 기초 트레이닝: 조건에 맞게 수열 변환하기 2

import Foundation

func solution(_ arr:[Int]) -> Int {
    var result: [Int] = arr
    var answer: Int = 0
    while true {
        let next_result: [Int] = result.map { num -> Int in
            if num >= 50 && num % 2 == 0 {
                return num / 2
            }
            else if num < 50 && num % 2 == 1 {
                return num * 2 + 1
            }
            return num
        }
        if result == next_result {
            break
        }
        result = next_result
        answer += 1
    }
    
    return answer
}