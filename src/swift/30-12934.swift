// https://school.programmers.co.kr/learn/courses/30/lessons/12934
// 연습문제: 정수 제곱근 판별

func solution(_ n:Int64) -> Int64 {
    let x = Int64(Double(n).squareRoot())
    if x * x == n {
        return (x + 1) * (x + 1)
    }
    return -1
}