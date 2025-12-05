// https://school.programmers.co.kr/learn/courses/30/lessons/131705
// 삼총사

import Foundation

func solution(_ number:[Int]) -> Int {
    let n: Int = number.count
    var answer: Int = 0
    for i in 0..<n {
        for j in i+1..<n {
            for k in j+1..<n {
                if number[i] + number[j] + number[k] == 0 {
                    print(i, j, k)
                    answer += 1
                }
            }
        }
    }
    return answer
}