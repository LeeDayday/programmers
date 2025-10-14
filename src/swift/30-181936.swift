// https://school.programmers.co.kr/learn/courses/30/lessons/181936
// 코딩 기초 트레이닝

import Foundation

func solution(_ number:Int, _ n:Int, _ m:Int) -> Int {
    if number % n == 0 && number % m == 0 {
        return 1
    }
    return 0
    
}