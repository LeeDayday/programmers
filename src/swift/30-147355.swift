// https://school.programmers.co.kr/learn/courses/30/lessons/147355
// 연습문제: 크기가 작은 부분 문자열

import Foundation

func solution(_ t:String, _ p:String) -> Int {
    let m: Int = p.count
    var s: String.Index = t.startIndex
    var e: String.Index = t.index(s, offsetBy: m)
    var answer: Int = 0

    while true {
        let tmp = t[s..<e] 
        if tmp <= p {              
            answer += 1
        }
        if e == t.endIndex { 
            break 
        }
        s = t.index(after: s)
        e = t.index(after: e)
    }
    return answer
}