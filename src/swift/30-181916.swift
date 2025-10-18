// https://school.programmers.co.kr/learn/courses/30/lessons/181916
// 코딩 기초 트레이닝: 주사위 게임 3

import Foundation

func solution(_ a:Int, _ b:Int, _ c:Int, _ d:Int) -> Int {
    var counter:[Int:Int] = [:]
    counter[a, default: 0] += 1
    counter[b, default: 0] += 1
    counter[c, default: 0] += 1
    counter[d, default: 0] += 1
    
    switch counter.count {
        case 1:
            return 1111 * a
        case 4:
            return [a, b, c, d].min()!
        case 2:
            // (3, 1) 인 경우
            if counter.values.contains(3) {
                let p = counter.first(where: { $0.value == 3 })!.key
                let q = counter.first(where: { $0.value == 1 })!.key
                return (10 * p + q) * (10 * p + q)
            }
            // (2, 2) 인 경우
            else {
                let keys = Array(counter.keys)
                return (keys[0] + keys[1]) * abs(keys[0] - keys[1])
            }
        case 3:
            // (2, 1, 1) 인 경우
            let qr = counter.filter { $0.value == 1 }.map{ $0.key }
            return qr[0] * qr[1]
        default:
            return 0
    }

}