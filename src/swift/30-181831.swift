// https://school.programmers.co.kr/learn/courses/30/lessons/181831
// 코딩 기초 트레이닝: 특별한 이차원 배열 2

import Foundation

func solution(_ arr:[[Int]]) -> Int {
    let n: Int = arr.count
    for i in 0..<n {
        for j in i+1..<n {
            if arr[i][j] != arr[j][i] {
                return 0
            }
        }
    }
    return 1
}