// https://school.programmers.co.kr/learn/courses/30/lessons/12922
// 연습문제: 수박수박수박수박수박수?

func solution(_ n:Int) -> String {
    (1...n).map { $0 % 2 == 1 ? "수" : "박" }.joined()
}