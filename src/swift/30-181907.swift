// https://school.programmers.co.kr/learn/courses/30/lessons/181907
// 코딩 기초 트레이닝: 문자열의 앞의 n글자

import Foundation

func solution(_ my_string:String, _ n:Int) -> String {
    let startIndex: String.Index = my_string.startIndex
    let index: String.Index = my_string.index(startIndex, offsetBy: n)
    return String(my_string[..<index])
}