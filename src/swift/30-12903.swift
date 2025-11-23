// https://school.programmers.co.kr/learn/courses/30/lessons/12903
// 연습문제: 가운데 글자 가져오기

func solution(_ s:String) -> String {
    let idx: String.Index = s.index(s.startIndex, offsetBy: (s.count / 2))
    
    if s.count % 2 == 1 {
        return String(s[idx]) 
    }
    return String(s[s.index(before:idx)...idx])
    
}