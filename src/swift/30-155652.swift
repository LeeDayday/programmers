// https://school.programmers.co.kr/learn/courses/30/lessons/155652
// 연습문제: 둘만의 암호

import Foundation

func solution(_ s:String, _ skip:String, _ index:Int) -> String {
    let aValue: UInt8 = Character("a").asciiValue! // a의 ascii value
    let zValue: UInt8 = Character("z").asciiValue! // z의 ascii value
    
    var data: [Character] = [] // 변환가능한 알파벳
    var answer: String = ""
    
    for value in aValue...zValue {
        if !skip.contains(Character(Unicode.Scalar(value))) {
            data.append(Character(Unicode.Scalar(value)))
        }
    }
    
    let n: Int = data.count
    for ch in s {
        let idx = data.firstIndex(of: ch)!
        // print(data[(idx + index) % n], type(of: data[(idx + index) % n]))
        answer += String(data[(idx + index) % n])
    }
    
    
    return answer
}