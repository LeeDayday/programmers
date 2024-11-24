# https://school.programmers.co.kr/learn/courses/30/lessons/181840
# 코딩 기초 트레이닝

import Foundation

func solution(_ num_list:[Int], _ n:Int) -> Int {
    var answer: Int = 0
    for num in num_list {
        if num == n {
            answer = 1
            break
        }
    }
    return answer
}