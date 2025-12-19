// https://school.programmers.co.kr/learn/courses/30/lessons/12901
// 연습문제: 2016년

func daysOfMonth(_ month: Int) -> Int {
    switch month {
        case 1, 3, 5, 7, 8, 10, 12:
            return 31
        case 2:
            return 29
        default: 
            return 30
    }
}

func solution(_ a:Int, _ b:Int) -> String {
    var days: Int = 0
    let data: [String] = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]

    for month in 1..<a {
        days += daysOfMonth(month)
    }
    days += b - 1
    
    return data[days % 7]
}