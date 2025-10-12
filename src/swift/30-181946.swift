# https://school.programmers.co.kr/learn/courses/30/lessons/181946
# 코딩 기초 트레이닝

import Foundation

let inp = readLine()!.components(separatedBy: [" "]).map { $0 }
let (s1, s2) = (inp[0], inp[1])

print("\(s1)\(s2)")