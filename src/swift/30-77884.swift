// https://school.programmers.co.kr/learn/courses/30/lessons/77884
// 월간 코드 챌린지 시즌2: 약수의 개수와 덧셈

import Foundation

func solution(_ left:Int, _ right:Int) -> Int {
    var answer: Int = 0
    for num in left...right {
        let root = Int(Double(num).squareRoot())
        if root * root == num { // 제곱수: 약수의 개수가 홀수
            answer -= num
        }
        else {
            answer += num
        }
    }
    return answer
}
