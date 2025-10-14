// https://school.programmers.co.kr/learn/courses/30/lessons/181934
// 코딩 기초 트레이닝

import Foundation

func solution(_ ineq:String, _ eq:String, _ n:Int, _ m:Int) -> Int {
    let op = ineq + (eq == "=" ? "=" : "")   // ">", ">=", "<", "<=" 네 가지로 정규화
    let ok: Bool
    switch op {
        case ">=": ok = n >= m
        case ">":  ok = n > m
        case "<=": ok = n <= m
        case "<":  ok = n < m
        default:   ok = false                   
    }
    return ok ? 1 : 0
}