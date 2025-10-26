// https://school.programmers.co.kr/learn/courses/30/lessons/181873
// 코딩 기초 트레이닝: 특정한 문자를 대문자로 바꾸기

import Foundation

func solution(_ my_string:String, _ alp:String) -> String {
    let answer = my_string.map { ch -> Character in 
        if ch == Character(alp) { return Character(String(ch).uppercased()) }
        return ch
    }
    return String(answer)
}