// https://school.programmers.co.kr/learn/courses/30/lessons/181898
// 코딩 기초 트레이닝: 가까운 1 찾기

import Foundation

func solution(_ arr:[Int], _ idx:Int) -> Int {
    for i in idx..<arr.count {
        if arr[i] == 1 {
            return i
        }
    }
    return -1
}