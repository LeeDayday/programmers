// https://school.programmers.co.kr/learn/courses/30/lessons/12940
// 연습문제: 최대공약수와 최소공배수

func solution(_ n:Int, _ m:Int) -> [Int] {
    var gcd: Int = 1 // 최대공약수
    for num in 2...min(n, m) {
        if n % num == 0 && m % num == 0 {
            gcd = num
        }
    }
    return gcd == 1 ? [gcd, n * m] : [gcd, n * m / gcd]
}