// https://school.programmers.co.kr/learn/courses/30/lessons/133499
// 연습문제: 옹알이 (2)

import Foundation

func solution(_ babbling:[String]) -> Int {
    var answer: Int = 0
    let data: [String] = ["aya", "ye", "woo", "ma"]
    let forbidden: [String] = ["ayaaya", "yeye", "woowoo", "mama"] // 연속해서 같은 발음 
    
    for word in babbling {
        var i = word.startIndex
        var prev = ""
        var speak = true

        while i < word.endIndex {
            var matched = false

            for possibleWord in data {
                if possibleWord == prev { continue } // 연속 같은 발음 금지

                if word[i...].hasPrefix(possibleWord) {
                    i = word.index(i, offsetBy: possibleWord.count)
                    prev = possibleWord
                    matched = true
                    break
                }
            }

            if !matched { 
                speak = false
                break 
            }
        }

        if speak { 
            answer += 1 
        }
    }
    return answer
}