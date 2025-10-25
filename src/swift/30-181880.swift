// https://school.programmers.co.kr/learn/courses/30/lessons/181880
// 코딩 기초 트레이닝: 1로 만들기

import Foundation

func solution(_ num_list:[Int]) -> Int {
    var answer: Int = 0
    for i in 0..<num_list.count {
        var tmp: Int = num_list[i]
        while tmp != 1 {
            if tmp % 2 == 0 {
                tmp = tmp / 2
            }
            else {
                tmp = (tmp - 1) / 2
            }
            answer += 1
        }
    }
    return answer
}