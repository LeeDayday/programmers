// https://school.programmers.co.kr/learn/courses/30/lessons/181932
// 코딩 기초 트레이닝

import Foundation

func solution(_ code:String) -> String {
    var mode: Int = 0
    var ret: String = ""
    for (idx, ch) in code.enumerated() {
        if mode == 0 {
            if ch != "1" {
                if idx % 2 == 0 {
                    ret.append(ch)
                }
            }
            else {
                mode = 1
            }
        }
        else {
            if ch != "1" {
                if idx % 2 == 1 {
                    ret.append(ch)
                }
            }
            else {
                mode = 0
            }
        }
    }
    if ret == "" {
        return "EMPTY"
    }
    return ret
}