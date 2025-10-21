// https://school.programmers.co.kr/learn/courses/30/lessons/181901
// 코딩 기초 트레이닝: 배열 만들기 1

import Foundation

func solution(_ n:Int, _ k:Int) -> [Int] {
    var answer: [Int] = []
    for num in stride(from: k, through: n, by: k) {
        answer.append(num)
    }
    return answer
}