// https://school.programmers.co.kr/learn/courses/30/lessons/181866
// 코딩 기초 트레이닝: 문자열 잘라서 정렬하기

import Foundation

func solution(_ myString:String) -> [String] {
    return myString.split(separator: "x").sorted().map{ String($0) }
}