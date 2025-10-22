// https://school.programmers.co.kr/learn/courses/30/lessons/181893
// 코딩 기초 트레이닝: 배열 조각하기

import Foundation

func solution(_ arr:[Int], _ query:[Int]) -> [Int] {
    var l = 0
    var r = arr.count - 1
    
    for (i, q) in query.enumerated() {
        if i % 2 == 0 {
            r = l + q
        } else {
            l = l + q
        }
    }
    
    return l <= r ? Array(arr[l...r]) : []
}