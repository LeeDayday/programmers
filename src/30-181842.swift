# https://school.programmers.co.kr/learn/courses/30/lessons/181842
# 코딩 기초 트레이닝

import Foundation

func solution(_ str1:String, _ str2:String) -> Int {
    if str2.contains(str1) {
        return 1
    }
    return 0
}