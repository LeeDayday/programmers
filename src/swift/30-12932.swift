// https://school.programmers.co.kr/learn/courses/30/lessons/12932
// 연습문제: 자연수 뒤집어 배열로 만들기

func solution(_ n:Int64) -> [Int] {
    var number = n
    var answer: [Int] = []
    while number > 0 {
        answer.append(Int(number % 10))
        number /= 10
    }
    return answer
}
