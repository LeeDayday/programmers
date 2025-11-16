// https://school.programmers.co.kr/learn/courses/30/lessons/12916
// 연습문제: 문자열 내 p와 y의 개수

import Foundation

func solution(_ s:String) -> Bool
{
    let lower: String = s.lowercased()
    return lower.filter { $0 == "p" }.count == lower.filter { $0 == "y" }.count
}