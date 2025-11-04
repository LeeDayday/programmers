// https://school.programmers.co.kr/learn/courses/30/lessons/181829
// 코딩 기초 트레이닝: 이차원 배열 대각선 순회하기

import Foundation

func solution(_ board:[[Int]], _ k:Int) -> Int {
    var answer: Int = 0
    let n: Int = board.count
    let m: Int = board[0].count
    for i in 0..<n {
        for j in 0..<m {
            if i + j <= k {
                answer += board[i][j]
            }
        }
    }
    return answer
}