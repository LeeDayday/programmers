// https://school.programmers.co.kr/learn/courses/30/lessons/12977
// Summer/Winter Coding(~2018): 소수 만들기

import Foundation


func isPrime(_ num: Int) -> Bool {
    if num == 1 { return false }
    
    for i in 2..<num {
        if num % i == 0 {
            return false
        }
    }
    return true
}

func solution(_ nums:[Int]) -> Int {
    var answer = 0
    let n: Int = nums.count
    
    for i in 0 ..< n - 2 {
        for j in i + 1 ..< n - 1 {
            for k in j + 1 ..< n {
                if isPrime(nums[i] + nums[j] + nums[k]) {
                    answer += 1
                }
            }
        }
    }
    return answer
}