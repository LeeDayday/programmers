// https://school.programmers.co.kr/learn/courses/30/lessons/181912
// 코딩 기초 트레이닝: 배열 만들기 5

import Foundation

func solution(_ intStrs:[String], _ k:Int, _ s:Int, _ l:Int) -> [Int] {
    var answer: [Int] = []
    for str in intStrs {
        // 범위 체크 (s부터 l개가 문자열 길이를 넘지 않는지)
        guard s >= 0, l >= 0, s + l <= str.count else { continue }

        let start = str.index(str.startIndex, offsetBy: s)
        let end   = str.index(start, offsetBy: l)          // s..<(s+l)
        let slice = String(str[start..<end])                // 부분 문자열

        if let val = Int(slice), val > k {                  // 안전 언래핑 후 비교
            answer.append(val)
        }
    }
    return answer
}