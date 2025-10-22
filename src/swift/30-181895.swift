// https://school.programmers.co.kr/learn/courses/30/lessons/181895
// 코딩 기초 트레이닝: 배열 만들기 3

import Foundation

func solution(_ arr:[Int], _ intervals:[[Int]]) -> [Int] {
    var answer: [Int] = []
    for interval in intervals {
        let x: Int = interval[0]
        let y: Int = interval[1]
        answer += arr[x...y]
    }
    return answer
}