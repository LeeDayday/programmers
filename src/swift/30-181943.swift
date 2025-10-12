# https://school.programmers.co.kr/learn/courses/30/lessons/181943
# 코딩 기초 트레이닝

import Foundation

func solution(_ my_string:String, _ overwrite_string:String, _ s:Int) -> String {
    let startIndex = my_string.startIndex
    let prefixPart = my_string[..<my_string.index(startIndex, offsetBy: s)]
    let suffixStart = my_string.index(startIndex, offsetBy: s + overwrite_string.count)
    let suffixPart = my_string[suffixStart...]
    return String(prefixPart) + overwrite_string + String(suffixPart)
}