// https://school.programmers.co.kr/learn/courses/30/lessons/181930
// 코딩 기초 트레이닝

import Foundation

import Foundation

func solution(_ a:Int, _ b:Int, _ c:Int) -> Int {
    let s1:Int = a + b + c
    let s2:Int = a*a + b*b + c*c
    let s3:Int = a*a*a + b*b*b + c*c*c
    switch Set([a, b, c]).count {
        case 3:
            return s1        
        case 1:
            return s1 * s2 * s3
        default:
            return s1 * s2
        
    }

}