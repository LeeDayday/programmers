// https://school.programmers.co.kr/learn/courses/30/lessons/181905
// 코딩 기초 트레이닝: 문자열 뒤집기

import Foundation

func solution(_ my_string:String, _ s:Int, _ e:Int) -> String {
    var answer:[Character] = Array(my_string)
    let reveresedSub = answer[s...e].reversed()
    answer.replaceSubrange(s...e, with: reveresedSub)
    return String(answer)
}