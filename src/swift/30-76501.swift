// https://school.programmers.co.kr/learn/courses/30/lessons/76501
// 월간 코드 챌린지 시즌2: 음양 더하기

import Foundation

func solution(_ absolutes:[Int], _ signs:[Bool]) -> Int {
    zip(absolutes, signs)
        .map{ $1 ? $0: -$0 }
        .reduce(0, +)
}