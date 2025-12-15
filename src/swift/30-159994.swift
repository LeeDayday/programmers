// https://school.programmers.co.kr/learn/courses/30/lessons/159994
// 연습문제: 카드 뭉치

import Foundation

func solution(_ cards1:[String], _ cards2:[String], _ goal:[String]) -> String {
    var idx1: Int = 0
    var idx2: Int = 0
    var result: Bool = true
    for word in goal {
        if idx1 < cards1.count && word == cards1[idx1] {
            idx1 += 1
        }
        else if idx2 < cards2.count && word == cards2[idx2] {
            idx2 += 1
        }
        else {
            result = false
            break
        }
    }
    return result ? "Yes" : "No"
}