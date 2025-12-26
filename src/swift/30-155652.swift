// https://school.programmers.co.kr/learn/courses/30/lessons/155652
// 연습문제: 둘만의 암호

import Foundation

func solution(_ s:String, _ skip:String, _ index:Int) -> String {
    let skipSet: Set<Character> = Set(skip)
    let aValue: UInt8 = Character("a").asciiValue! // a의 ascii value
    let zValue: UInt8 = Character("z").asciiValue! // z의 ascii value
    
    var data: [Character] = [] // 변환가능한 알파벳
    var answer: String = ""
    
    // 변환 가능한 알파벳 구하기
    for value in aValue...zValue {
        let ch = Character(Unicode.Scalar(Int(value))!)
        if !skip.contains(ch) {
            data.append(ch)
        }
    }
    
    // 알파벳 별 인덱스 매핑하기
    var alphaDict: [Character: Int] = [:] // 알파벳 별 인덱스
    for (i, ch) in data.enumerated() {
        alphaDict[ch] = i
    }
    
    let n: Int = data.count
    for ch in s {
        let idx = alphaDict[ch]!
        answer.append(data[(idx + index) % n])
    }
    
    
    return answer
}