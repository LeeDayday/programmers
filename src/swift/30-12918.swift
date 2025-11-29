// https://school.programmers.co.kr/learn/courses/30/lessons/12918
// 연습문제: 문자열 다루기 기본

func solution(_ s:String) -> Bool {
    if s.count == 4 || s.count == 6 {
        guard let _ = Int(s) else { return false }
        return true
    }
    return false
}