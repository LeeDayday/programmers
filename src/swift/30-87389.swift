// https://school.programmers.co.kr/learn/courses/30/lessons/87389
// 월간 코드 챌린지 시즌3: 나머지가 1이 되는 수 찾기

import Foundation

func solution(_ n:Int) -> Int {
    var x: Int = 1
    while n % x != 1 {
        x += 1
    }
    return x
}