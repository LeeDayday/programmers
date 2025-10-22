// https://school.programmers.co.kr/learn/courses/30/lessons/181894
// 코딩 기초 트레이닝: 2의 영역

import Foundation

func solution(_ arr:[Int]) -> [Int] {
    var firstIndex = arr.firstIndex(of: 2)
    if firstIndex == nil {
        return [-1]
    }    
    var lastIndex = arr.lastIndex(of: 2)

    return Array(arr[firstIndex!...lastIndex!])
}