// https://school.programmers.co.kr/learn/courses/30/lessons/12935
// 연습문제: 제일 작은 수 제거하기

func solution(_ arr:[Int]) -> [Int] {
    let minValue: Int = arr.min()!
    let answer: [Int] = arr.filter { $0 != minValue }
    return answer.isEmpty ? [-1] : answer
}