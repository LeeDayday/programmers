# https://school.programmers.co.kr/learn/courses/30/lessons/181949
# 코딩 기초 트레이팅

import Foundation

let s1 = readLine()!

for ch in s1 {
    if "a" <= ch && ch <= "z" {
        print(ch.uppercased(), terminator: "")
    }
    else {
        print(ch.lowercased(), terminator: "")
    }
}
