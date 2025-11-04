// https://school.programmers.co.kr/learn/courses/30/lessons/181830
// 코딩 기초 트레이닝: 정사각형으로 만들기

import Foundation

func solution(_ arr:[[Int]]) -> [[Int]] {
    let n: Int = arr.count
    let m: Int = arr[0].count
    
    var answer: [[Int]] = arr
    
    if n > m { // 열 > 행
        for i in 0..<n {
            answer[i].append(contentsOf: Array(repeating: 0, count: n - m))
        }
    }
    else {
        for i in 0..<(m-n) {
            answer.append(Array(repeating: 0, count: m))
        }
    } 
    return answer
}