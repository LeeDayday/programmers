// https://school.programmers.co.kr/learn/courses/30/lessons/181847
// 코딩 기초 트레이닝: 0 떼기

import Foundation

func solution(_ n_str:String) -> String {
    var s: String.Index = n_str.startIndex
    while n_str[s] == "0" {
        s = n_str.index(after: s)
    }
    return String(n_str[s...])
}