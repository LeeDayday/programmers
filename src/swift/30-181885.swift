// https://school.programmers.co.kr/learn/courses/30/lessons/181885
// 코딩 기초 트레이닝: 할 일 목록

import Foundation

func solution(_ todo_list:[String], _ finished:[Bool]) -> [String] {
    var answer: [String] = []
    for (t, f) in zip(todo_list, finished) {
        if !f {
            answer.append(t)
        }
    }
    return answer
}