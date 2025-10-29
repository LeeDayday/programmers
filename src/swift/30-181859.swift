// https://school.programmers.co.kr/learn/courses/30/lessons/181859
// 코딩 기초 트레이닝: 배열 만들기 6

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
            if stk.last == arr[i] {
                stk.popLast()
                i += 1
            }
            else {
                stk.append(arr[i])
                i += 1
            }
        }
    }
    if stk.isEmpty {
        return [-1]
    }
    return stk
}