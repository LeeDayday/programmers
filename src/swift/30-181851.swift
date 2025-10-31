// https://school.programmers.co.kr/learn/courses/30/lessons/181851
// 코딩 기초 트레이닝: 전국 대회 선발 고사

import Foundation

func solution(_ rank:[Int], _ attendance:[Bool]) -> Int {
    let top3 = rank.enumerated()
    .filter { attendance[$0.offset] }
    .sorted(by: { $0.element < $1.element })
    .prefix(3)
    .map(\.offset)
    return 10000 * top3[0] + 100 * top3[1] + top3[2]
}