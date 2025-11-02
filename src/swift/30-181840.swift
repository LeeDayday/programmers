// https://school.programmers.co.kr/learn/courses/30/lessons/181840
// 코딩 기초 트레이닝: 정수 찾기

import Foundation

func solution(_ num_list:[Int], _ n:Int) -> Int {
    if num_list.contains(n) {
        return 1
    }
    return 0
}