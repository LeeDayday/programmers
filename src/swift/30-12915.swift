// https://school.programmers.co.kr/learn/courses/30/lessons/12915
// 연습문제: 문자열 내 마음대로 정렬하기

func solution(_ strings:[String], _ n:Int) -> [String] {
    strings.sorted {
        let i: String.Index = $0.index($0.startIndex, offsetBy: n)
        let j: String.Index = $1.index($1.startIndex, offsetBy: n)
        
        if $0[i] != $1[j] {
            return $0[i] < $1[i] // n번째 글자를 기준으로 정렬
        }
        return $0 < $1 // n번째 글자가 같은 문자열이 여럿일 경우, 사전순으로 정렬
    }
}