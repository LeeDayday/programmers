// https://school.programmers.co.kr/learn/courses/30/lessons/12930
// 연습문제: 이상한 문자 만들기

func solution(_ s:String) -> String {
    var answer = ""
    var idx: Int = 0
    for ch in s {
        if ch == " " {
            answer.append(" ")
            idx = 0
            continue
        }
        else if idx % 2 == 0 {
            answer.append(Character(ch.uppercased()))
        }
        else {
            answer.append(Character(ch.lowercased()))
        }
        idx += 1
    }
    return answer
}