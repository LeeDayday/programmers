// https://school.programmers.co.kr/learn/courses/30/lessons/181911
// 코딩 기초 트레이닝: 부분 문자열 이어 붙여 문자열 만들기

import Foundation

func solution(_ my_strings:[String], _ parts:[[Int]]) -> String {
    var answer: String = ""
    for (str, part) in zip(my_strings, parts) {
        let start = str.index(str.startIndex, offsetBy: part[0])
        let end = str.index(str.startIndex, offsetBy: part[1])
        answer.append(String(str[start...end]))
    }
    return answer
}