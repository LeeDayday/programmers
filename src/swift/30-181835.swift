# https://school.programmers.co.kr/learn/courses/30/lessons/181835
# 코딩 기초 트레이닝

import Foundation

func solution(_ arr:[Int], _ k:Int) -> [Int] {
    if k % 2 == 0 
        return arr.map { $0 + k }
    
    else 
        return arr.map { $0 * k }
    
}