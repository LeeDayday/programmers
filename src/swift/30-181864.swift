// https://school.programmers.co.kr/learn/courses/30/lessons/181864
// 코딩 기초 트레이닝: 문자열 바꿔서 찾기

import Foundation

func solution(_ myString:String, _ pat:String) -> Int {
    if myString.contains(String(pat.map{ $0 == "A" ? "B" : "A"})) {
        return 1
    }
    return 0
}