// https://school.programmers.co.kr/learn/courses/30/lessons/181926
// 코딩 기초 트레이닝: 수 조작하기 1

import Foundation

func solution(_ n:Int, _ control:String) -> Int {
    var answer:Int = n
    for cmd in control {
        switch cmd {
            case "w":
                answer += 1
            case "s":
                answer -= 1
            case "d":
                answer += 10
            default:
                answer -= 10
        }
    }
    return answer
}