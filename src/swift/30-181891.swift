// https://school.programmers.co.kr/learn/courses/30/lessons/181891
// 코딩 기초 트레이닝: 순서 바꾸기

import Foundation

func solution(_ num_list:[Int], _ n:Int) -> [Int] {
    return Array(num_list[(n - 1)...])
}