# https://school.programmers.co.kr/learn/courses/30/lessons/181950
# 코딩 기초 트레이닝

import Foundation

let inp = readLine()!.components(separatedBy: [" "]).map { $0 }
let (s1, a) = (inp[0], Int(inp[1])!)

for _ in 1 ... a {
    print(s1, terminator: "")
}
