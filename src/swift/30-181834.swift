// https://school.programmers.co.kr/learn/courses/30/lessons/181834
// 코딩 기초 트레이닝: l로 만들기

import Foundation

func solution(_ myString:String) -> String {
    return myString.map { $0 < "l" ? "l" : $0 }.map(String.init).joined()
}