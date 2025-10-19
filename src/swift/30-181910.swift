// https://school.programmers.co.kr/learn/courses/30/lessons/181910
// 코딩 기초 트레이닝: 문자열의 뒤의 n글자

import Foundation

func solution(_ my_string:String, _ n:Int) -> String {
    let length: Int = my_string.count
    let start: String.Index = my_string.index(my_string.startIndex, offsetBy: length - n)
    return String(my_string[start...])
}