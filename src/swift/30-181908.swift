// https://school.programmers.co.kr/learn/courses/30/lessons/181908
// 코딩 기초 트레이닝: 접미사인지 확인하기

import Foundation

func solution(_ my_string:String, _ is_suffix:String) -> Int {
    for i in 0..<my_string.count {
        let start: String.Index = my_string.index(my_string.startIndex, offsetBy: i)
        let result: String = String(my_string[start...])
        if result == is_suffix {
            return 1
        }
    }
    return 0
}