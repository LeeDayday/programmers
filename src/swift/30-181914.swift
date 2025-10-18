// https://school.programmers.co.kr/learn/courses/30/lessons/181914
// 코딩 기초 트레이닝: 9로 나눈 나머지

import Foundation

func solution(_ number:String) -> Int {
    var answer: Int = 0
    for num in number {
        answer += Int(String(num)) ?? 0
    }
    return answer % 9
}