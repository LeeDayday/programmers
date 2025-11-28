//https://school.programmers.co.kr/learn/courses/30/lessons/82612
// 위클리 챌린지: 부족한 금액 계산하기

import Foundation

func solution(_ price:Int, _ money:Int, _ count:Int) -> Int64{
    let total: Int = (1...count).map { $0 * price }.reduce(0, +)
    return max(Int64(total) - Int64(money), Int64(0))
}