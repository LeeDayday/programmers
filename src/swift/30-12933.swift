// https://school.programmers.co.kr/learn/courses/30/lessons/12933
// 연습문제: 정수 내림차순으로 배치하기

func solution(_ n:Int64) -> Int64 {
    var data = String(n).map { Int64(String($0))! }
    data.sort(by: >)
    return Int64(data.map(String.init).joined())!
}