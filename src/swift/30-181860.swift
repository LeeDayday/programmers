// https://school.programmers.co.kr/learn/courses/30/lessons/181860
// 코딩 기초 트레이닝: 빈 배열에 추가, 삭제하기

import Foundation

func solution(_ arr:[Int], _ flag:[Bool]) -> [Int] {
    var answer: [Int] = []
    for (num, bool) in zip(arr, flag) {
        if bool {
            for _ in 1...(num * 2) {
                answer.append(num)
            }
        }
        else {
            for _ in 1...num {
                answer.popLast()
            }
        }
    }
    return answer
}