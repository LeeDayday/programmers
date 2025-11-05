// https://school.programmers.co.kr/learn/courses/30/lessons/12931
// 연습 문제: 자릿수 더하기

import Foundation

func solution(_ n:Int) -> Int
{
    var answer:Int = 0
    var num: Int = n
    while num > 0 {
        answer += num % 10
        num /= 10
    }
    return answer
}