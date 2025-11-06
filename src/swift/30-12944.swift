// https://school.programmers.co.kr/learn/courses/30/lessons/12944
// 연습문제: 평균 구하기

func solution(_ arr:[Int]) -> Double {
    return Double(arr.reduce(0, +)) / Double(arr.count)
}