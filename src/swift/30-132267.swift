// https://school.programmers.co.kr/learn/courses/30/lessons/132267
// 연습문제: 콜라 문제

import Foundation

func solution(_ a:Int, _ b:Int, _ n:Int) -> Int {
    var empty: Int = n // 빈 병 개수
    var answer: Int = 0 // 새로 받은 콜라 개수
    while empty >= a {
        let cnt = empty / a // 빈 병 (a * cnt) 개와 새 병 (b * cnt) 개 교환
        if cnt > 0 {
            empty -= a * cnt
            answer += b * cnt
        }            
        empty += b * cnt // 새로 받은 병 모두 마시기

    }
    return answer
}