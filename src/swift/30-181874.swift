// https://school.programmers.co.kr/learn/courses/30/lessons/181874
// 코딩 기초 트레이닝: A 강조하기

import Foundation

func solution(_ myString:String) -> String {
    let answer = myString.map { ch -> Character in
        if ch == "a" { return "A" }
        if ch == "A" { return "A" }
        return Character(String(ch).lowercased())
    }
    return String(answer)
}