// https://school.programmers.co.kr/learn/courses/30/lessons/12947
// 연습문제: 하샤드 수

func solution(_ x:Int) -> Bool {
    var num: Int = String(x).map{ Int(String($0))! }.reduce(0, +)
    return x % num == 0 ? true : false
}