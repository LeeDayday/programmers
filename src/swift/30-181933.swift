// https://school.programmers.co.kr/learn/courses/30/lessons/181933
// 코딩 기초 트레이닝

import Foundation

func solution(_ a:Int, _ b:Int, _ flag:Bool) -> Int {
    if flag {
        return a + b
    }
    return a - b
}