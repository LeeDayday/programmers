// https://school.programmers.co.kr/learn/courses/30/lessons/12954
// 연습문제: x만큼 간격이 있는 n개의 숫자

func solution(_ x:Int, _ n:Int) -> [Int64] {
    return (1...n).map{ Int64(x) * Int64($0) }
}