// https://school.programmers.co.kr/learn/courses/30/lessons/12917
// 연습문제: 문자열 내림차순으로 배치하기

func solution(_ s:String) -> String {
    let data = s.map { String($0) }
    return data.sorted(by: >).joined()
}