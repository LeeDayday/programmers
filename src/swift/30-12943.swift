// https://school.programmers.co.kr/learn/courses/30/lessons/12943
// 연습문제: 클라츠 추측

func solution(_ num:Int) -> Int {
    var n: Int = num
    for i in 0..<500 {
        if n == 1 {
            return i
        }
        if n % 2 == 0 {
            n /= 2
        }
        else {
            n *= 3
            n += 1
        }
    }
    return -1
}