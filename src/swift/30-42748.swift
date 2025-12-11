// https://school.programmers.co.kr/learn/courses/30/lessons/42748
// 정렬: K번째 수

import Foundation

func solution(_ array:[Int], _ commands:[[Int]]) -> [Int] {
    var answer: [Int] = []
    for cmd in commands {
        let data: [Int] = array[(cmd[0] - 1)...(cmd[1] - 1)].sorted()
        answer.append(data[cmd[2]-1])
    }
    return answer
}