// https://school.programmers.co.kr/learn/courses/30/lessons/12910
// 연습문제: 나누어 떨어지는 숫자 배열

func solution(_ arr:[Int], _ divisor:Int) -> [Int] {
    var answer: [Int] = arr.filter { $0 % divisor == 0 }.sorted()
    return answer.isEmpty ? [-1] : answer
}