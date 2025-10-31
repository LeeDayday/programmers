// https://school.programmers.co.kr/learn/courses/30/lessons/181849
// 코딩 기초 트레이닝: 문자열 정수의 합

import Foundation

func solution(_ num_str:String) -> Int {
    return num_str.compactMap { Int(String($0)) }.reduce(0, +)
}