// https://school.programmers.co.kr/learn/courses/30/lessons/181843
// 코딩 기초 트레이닝: 부분 문자열인지 확인하기

import Foundation

func solution(_ my_string:String, _ target:String) -> Int {
    return my_string.contains(target) ? 1 : 0
}