// https://school.programmers.co.kr/learn/courses/30/lessons/181833
// 코딩 기초 트레이닝: 특별한 이차원 배열 1

import Foundation

func solution(_ n:Int) -> [[Int]] {
    (0..<n).map { i in
        (0..<n).map { j in i == j ? 1 : 0 }
    }
}