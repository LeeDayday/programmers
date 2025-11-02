// https://school.programmers.co.kr/learn/courses/30/lessons/181839
// 코딩 기초 트레이닝: 주사위 게임 1

import Foundation

func solution(_ a:Int, _ b:Int) -> Int {
    switch (a % 2, b % 2) {
        case (1, 1):
            return a * a + b * b
        
        case (0, 0):
            return abs(a - b)
        
        default:
            return 2 * (a + b)
        
    }
}