// https://school.programmers.co.kr/learn/courses/30/lessons/181906
// 코딩 기초 트레이닝: 접두사인지 확인하기

import Foundation

func solution(_ my_string:String, _ is_prefix:String) -> Int {
    // 길이 비교
    if my_string.count < is_prefix.count {
        return 0
    }
    // 앞에서부터 비교
    for (ch1, ch2) in zip(my_string, is_prefix) {
        if ch1 != ch2 {
            return 0
        }
    }
    return 1
}