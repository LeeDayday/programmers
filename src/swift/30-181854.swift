// https://school.programmers.co.kr/learn/courses/30/lessons/181854
// 코딩 기초 트레이닝: 배열의 길이에 따라 다른 연산하기

import Foundation

func solution(_ arr:[Int], _ n:Int) -> [Int] {
    let isOdd: Bool = arr.count % 2 == 1
    return arr.enumerated().map { (i, num) in
        if isOdd {
            return i % 2 == 0 ? num + n : num
        }
        else {
            return i % 2 == 1 ? num + n : num                        
        }
    }
}