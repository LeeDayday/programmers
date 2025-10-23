// https://school.programmers.co.kr/learn/courses/30/lessons/181890
// 코딩 기초 트레이닝: 왼쪽 오른쪽

import Foundation

func solution(_ str_list:[String]) -> [String] {
    for (i, ch) in str_list.enumerated() {
        if ch == "l" {
            if i > 0 {
                return Array(str_list[..<i])
            }
            return []
        }
        else if ch == "r" {
            if i + 1 < str_list.count {
                return Array(str_list[(i+1)...])
            }
            return []
        }
        
    }
    return []
}