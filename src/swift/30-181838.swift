// https://school.programmers.co.kr/learn/courses/30/lessons/181838
// 코딩 기초 트레이닝: 날짜 비교하기

import Foundation

func solution(_ date1:[Int], _ date2:[Int]) -> Int {
    return (date1[0], date1[1], date1[2]) < (date2[0], date2[1], date2[2]) ? 1 : 0
}