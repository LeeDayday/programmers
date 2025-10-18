// https://school.programmers.co.kr/learn/courses/30/lessons/181915
// 코딩 기초 트레이닝: 글자 이어 붙여 문자열 만들기

import Foundation

func solution(_ my_string:String, _ index_list:[Int]) -> String {
    var answer: String = ""
    let startIndex = my_string.startIndex

    for offset in index_list {
        let index = my_string.index(startIndex, offsetBy: offset)
        answer.append(my_string[index])
    }
    return answer
}