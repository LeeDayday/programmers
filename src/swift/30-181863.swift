// https://school.programmers.co.kr/learn/courses/30/lessons/181863
// 코딩 기초 트레이닝: rny_string

import Foundation

func solution(_ rny_string:String) -> String {
    return rny_string.replacingOccurrences(of: "m", with: "rn")
}