// https://school.programmers.co.kr/learn/courses/30/lessons/181832
// 코딩 기초 트레이닝: 정수를 나선형으로 배치하기

import Foundation

func solution(_ n:Int) -> [[Int]] {
    let dir = [(0, 1), (1, 0), (0, -1), (-1, 0)] // 오른쪽, 아래, 왼쪽, 위
    var answer: [[Int]] = Array(repeating: Array(repeating: 0, count: n), count: n)
    var x: Int = 0
    var y: Int = 0
    var idx: Int = 0
    
    var result: Int = 1
    for value in 1...(n * n) {
        answer[x][y] = value
        
        let next_x = x + dir[idx].0
        let next_y = y + dir[idx].1
        
        if (0 <= next_x && next_x < n) && (0 <= next_y && next_y < n) && (answer[next_x][next_y] == 0) {
            ()
        }
        else {
            idx = (idx + 1) % 4
        }
        x = x + dir[idx].0
        y = y + dir[idx].1
    }
  
    return answer
}