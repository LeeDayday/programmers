// https://school.programmers.co.kr/learn/courses/30/lessons/181841
// 코딩 기초 트레이닝: 꼬리 문자열

import Foundation

func solution(_ str_list:[String], _ ex:String) -> String {
    var answer: String = ""
    for str in str_list {
        if !str.contains(ex) {
            answer += str
        }
    }
    return answer
}