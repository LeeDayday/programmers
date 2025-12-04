// https://school.programmers.co.kr/learn/courses/30/lessons/12982
// Summer/Winter Coding (~2018): 예산

import Foundation

func solution(_ d:[Int], _ budget:Int) -> Int {
    var total: Int = budget
    var answer: Int = 0
    for num in d.sorted() {
        total -= num
        if total < 0 {
            break
        }
        answer += 1
    }
    return answer
}