// https://school.programmers.co.kr/learn/courses/30/lessons/181925
// 코딩 기초 트레이닝: 수 조작하기 2

import Foundation

func solution(_ numLog:[Int]) -> String {
    var answer:String = ""
    for i in 1..<numLog.count{
        switch numLog[i - 1] - numLog[i] {
            case 1:
                answer.append("s")
            case -1:
                answer.append("w")
            case 10:
                answer.append("a")
            default:
                answer.append("d")
        }
    }
    return answer
}