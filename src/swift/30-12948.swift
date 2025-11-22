// https://school.programmers.co.kr/learn/courses/30/lessons/12948
// 연습문제: 핸드폰 번호 가리기

func solution(_ phone_number:String) -> String {
    let n: Int = phone_number.count - 4
    let idx: String.Index = phone_number.index(phone_number.startIndex, offsetBy: n)
    return String(repeating: "*", count: n) + String(phone_number[idx...])
}