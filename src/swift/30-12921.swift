// https://school.programmers.co.kr/learn/courses/30/lessons/12921
// 연습문제: 소수 찾기

func isPrime(_ num: Int) -> Bool {
    if num == 1 { return false }
    if num == 2 { return true }
    if num % 2 == 0 { return false }
    var i: Int = 3
    
    while i * i <= num {
        if num % i == 0 { return false }
        i += 2
    }
    return true
}
func solution(_ n:Int) -> Int {
    (2...n).reduce(0) { $0 + (isPrime($1) ? 1 : 0) }
}