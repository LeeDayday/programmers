// https://school.programmers.co.kr/learn/courses/30/lessons/181846
// 코딩 기초 트레이닝: 두 수의 합

import Foundation

func solution(_ a:String, _ b:String) -> String {
    let A = Array(a.reversed())
    let B = Array(b.reversed())
    
    var extra: Int = 0
    var result: [Int] = []
    let maxLen: Int = max(A.count, B.count)
    
    for i in 0..<maxLen {
        let x = (i < A.count ? A[i].wholeNumberValue : nil) ?? 0
        let y = (i < B.count ? B[i].wholeNumberValue : nil) ?? 0
        let sum = x + y + extra
        result.append(sum % 10)
        extra = sum / 10
    }
    
    if extra > 0 {
        result.append(extra)
    }
    return result.reversed().map(String.init).joined()
}