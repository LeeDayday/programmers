// https://school.programmers.co.kr/learn/courses/30/lessons/136798
// 연습문제: 기사단원의 무기

import Foundation

func countDivisors(_ n: Int) -> Int {
    var answer: Int = 0
    var i: Int = 1
    while i * i <= n {
        if n % i == 0 {
            if i * i == n { // 제곱근인 경우
                answer += 1
            }
            else {
                answer += 2
            }
        }
        i += 1
    }
    return answer
}

func solution(_ number:Int, _ limit:Int, _ power:Int) -> Int {
    var answer: Int = 0
    for i in 1...number {
        let result: Int = countDivisors(i)
        answer += (result > limit) ? power : result
    }
    return answer
}