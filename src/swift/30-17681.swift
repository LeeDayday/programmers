// https://school.programmers.co.kr/learn/courses/30/lessons/17681
// 2018 KAKAO BLIND RECRUITMENT: [1차] 비밀지도

func solution(_ n:Int, _ arr1:[Int], _ arr2:[Int]) -> [String] {
    var answer: [String] = []
    
    for (num1, num2) in zip(arr1, arr2) {
        let binary = String(num1 | num2, radix: 2)
        let padded: String = String(repeating: "0", count: n - binary.count) + binary
        let result: String = String(padded.map { $0 == "1" ? "#" : " " })
        answer.append(result)
    }

    return answer
}