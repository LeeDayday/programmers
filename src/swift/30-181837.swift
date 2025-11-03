// https://school.programmers.co.kr/learn/courses/30/lessons/181837
// 코딩 기초 트레이닝: 커피 심부름

import Foundation

func solution(_ order:[String]) -> Int {
    var answer:Int = 0
    for str in order {
        if str.contains("americano") {
            answer += 4500
        }
        else if str.contains("latte") {
            answer += 5000
        }
        else {
            answer += 4500          
        }
    }
    return answer
}