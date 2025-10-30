// https://school.programmers.co.kr/learn/courses/30/lessons/181856
// 코딩 기초 트레이닝: 배열 비교하기

import Foundation

func solution(_ arr1:[Int], _ arr2:[Int]) -> Int {
    let n = arr1.count
    let m = arr2.count
    if n != m {
        return n > m ? 1 : -1
    }
    else {
        let sum1 = arr1.reduce(0, +)
        let sum2 = arr2.reduce(0, +)
        if sum1 > sum2 {
            return 1
        }
        else if sum1 < sum2{
            return -1
        }
    }
    return 0
}