// https://school.programmers.co.kr/learn/courses/30/lessons/181888
// 코딩 기초 트레이닝: n개 간격의 원소들

import Foundation

func solution(_ num_list:[Int], _ n:Int) -> [Int] {
    var answer: [Int] = []
    for i in stride(from: 0, to: num_list.count, by: n) {
        answer.append(num_list[i])
    }
    return answer
}