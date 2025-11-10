// https://school.programmers.co.kr/learn/courses/30/lessons/12928
// 연습문제: 약수의 합

func solution(_ n:Int) -> Int {
    if n == 0 {
        return 0
    }
    return (1...n).map { n % $0 == 0 ? $0 : 0 }.reduce(0, +)
}