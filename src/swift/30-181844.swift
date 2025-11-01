// https://school.programmers.co.kr/learn/courses/30/lessons/181844
// 코딩 기초 트레이닝: 배열의 원소 삭제하기

import Foundation

func solution(_ arr:[Int], _ delete_list:[Int]) -> [Int] {
    let delete_set: Set<Int> = Set(delete_list)
    var answer: [Int] = []
    
    for num in arr {
        if !delete_list.contains(num) {
            answer.append(num)
        }
    }
    return answer
}