// https://school.programmers.co.kr/learn/courses/30/lessons/181857
// 코딩 기초 트레이닝: 배열의 길이를 2의 거듭제곱으로 만들기

import Foundation

func solution(_ arr:[Int]) -> [Int] {
    let n = arr.count
    if (n > 0) && (n & (n - 1) == 0) {
        return arr
    }
    var target: Int = 1
    var answer: [Int] = arr
    while target < arr.count {
        target *= 2
    }
    answer.append(contentsOf: repeatElement(0, count: target - arr.count))
    return answer
}