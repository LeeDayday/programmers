// https://school.programmers.co.kr/learn/courses/30/lessons/181913
// 코딩 기초 트레이닝: 문자열 여러 번 뒤집기

import Foundation

func solution(_ my_string:String, _ queries:[[Int]]) -> String {
    var answer: [Character] = Array(my_string)
    
    for query in queries {
        let s = query[0], e = query[1]
        // 부분 구간 뒤집기
        let reversedSub = answer[s...e].reversed()
        answer.replaceSubrange(s...e, with: reversedSub)
    }
    return String(answer)
}