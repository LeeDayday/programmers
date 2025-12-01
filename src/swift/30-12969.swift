// https://school.programmers.co.kr/learn/courses/30/lessons/12969
// 연습문제: 직사각형 별찍기

import Foundation

let n = readLine()!.components(separatedBy: [" "]).map { Int($0)! }
let (a, b) = (n[0], n[1])

for _ in 1...b {
    for _ in 1...a {
        print("*", terminator: "")
    }
    print()
}