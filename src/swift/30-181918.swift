// https://school.programmers.co.kr/learn/courses/30/lessons/181918
// 코딩 기초 트레이닝: 배열 만들기 4

import Foundation

func solution(_ arr:[Int]) -> [Int] {
    var stk: [Int] = []
    var i: Int = 0
    
    while i < arr.count {
        if stk.isEmpty {
            stk.append(arr[i])
            i += 1
        }
        else {
            if stk[stk.count - 1] < arr[i] {
                stk.append(arr[i])
                i += 1
            }
            else {
                stk.popLast()
            }
        }
    }
    return stk
}
