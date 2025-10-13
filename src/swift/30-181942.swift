// https://school.programmers.co.kr/learn/courses/30/lessons/181942
// 코딩 기초 트레이닝

import Foundation

func solution(_ str1:String, _ str2:String) -> String {
    var answer:String = ""

    for (ch1, ch2) in zip(str1, str2) {
        answer.append(ch1)
        answer.append(ch2)
    }
    return answer
}