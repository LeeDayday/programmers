// https://school.programmers.co.kr/learn/courses/30/lessons/12912
// 연습문제: 두 정수 사이의 합

func solution(_ a:Int, _ b:Int) -> Int64 {
    var answer: Int64 = 0
    for num in (min(a, b))...(max(a, b)) {
        answer += Int64(num)
    }
    return answer
}