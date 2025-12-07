// https://school.programmers.co.kr/learn/courses/30/lessons/12926
// 연습문제: 시저 암호

import Foundation

func solution(_ s: String, _ n: Int) -> String {
    var answer:String = ""
    let aValue:Int = Int(UnicodeScalar("a").value)
    let AValue:Int = Int(UnicodeScalar("A").value)

    for ch in s {
        if ch == " " {
            answer.append(" ")
            continue
        }
        let currValue = Int(UnicodeScalar(String(ch))!.value)
        let baseValue = ch.isLowercase ? aValue : AValue
        let newValue = baseValue + (currValue - baseValue + n) % 26
        
        answer.append(Character(UnicodeScalar(newValue)!))
    }
        
    return answer
}
