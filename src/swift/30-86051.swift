// https://school.programmers.co.kr/learn/courses/30/lessons/86051
// 월간 코드 챌린지 시즌 3: 없는 숫자 더하기

import Foundation

func solution(_ numbers:[Int]) -> Int {
    (0...9).filter{ !numbers.contains($0) }.reduce(0, +)
}